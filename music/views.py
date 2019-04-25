from django.http import HttpResponse
from .models import Album
from django.shortcuts import render, get_object_or_404
from django.http import Http404


# from django.template import loader

def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('')
    # context = {
    #     'all_album': all_albums,
    # }
    return render(request, 'music/index.html', {'all_album': all_albums})
    # html = ''
    # for album in all_album:
    #     url='/music/' + str(album_id) + '/'
    #     html += '<a href = "' + url + '">'> + album.album_title + '</a><br>'
    # return HttpResponse(template.render(context,request))


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    # return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exit")
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',
                      {'album': album, 'error message': "you did not selected a valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
    
    
    class SuggestedProductView(APIView):
    """
    You can get the Suggested Product for product.
     datetime.now(timezone.utc)
    """
    queryset = Products.objects.all()


    def get(self, request):

        validated_data=request.data
        cart_data = ShoppingCartProducts.objects.all()
        for cart in cart_data:
            cart_date = datetime.datetime.now(datetime.timezone.utc) - cart.created_date
            if cart_date.days > 7 :
                cart.product.discountper = 10

            # if cart_date > 7:
            #     pass


        code=validated_data.get('code')
        if code=="sumit123":
            products = self.queryset.filter(is_deleted=False, is_active=True)
            for product in products:
                product.discountper = 10
        else:
            products = self.queryset.filter(is_deleted=False, is_active=True)
        #products = self.queryset.exclude(discountper=00)

        json_data_product = ProductDiscountSerializer(products, many=True).data

        # import pdb;pdb.set_trace()

        # products = self.queryset.filter(is_deleted=False, is_active=True,show_to_my_blent=True)
        #
        # json_data_product = SuggestedProductSerializer(products, many=True).data
        #
        #
        # variant_info = ProductVariants.objects.filter(product__is_deleted=False, product__is_active=True, show_to_my_blent=True)
        #
        # json_data_variant = SuggestedProductVariantSerializer(variant_info, many = True).data
        #
        # json_data = json_data_product + json_data_variant
        #
        # #json_data = sorted(json_data,key=itemgetter('name'),reverse=True)
        # json_data = sorted(json_data, key=lambda k: k['name'])



        return JsonResponse({'success': True, 'message': 'Suggested Products fetched successfully.', 'data': json_data_product,'code':code})


class DiscountView(APIView):
    """
    You can get the Discount Product for product.
    """
    queryset = Products.objects.all()


    def get(self, request):
        #import pdb;pdb.set_trace()
        # pt=Products.objects.all().exclude(discountper=00)

        products = self.queryset.exclude(discountper=00)

        json_data_product = ProductDiscountSerializer(products, many=True).data


        # variant_info = ProductVariants.objects.filter(product__is_deleted=False, product__is_active=True, show_to_my_blent=True)
        #
        # json_data_variant = SuggestedProductVariantSerializer(variant_info, many = True).data
        #
        # json_data = json_data_product + json_data_variant
        #
        # #json_data = sorted(json_data,key=itemgetter('name'),reverse=True)
        # json_data = sorted(json_data, key=lambda k: k['name'])



        return JsonResponse({'success': True, 'message': 'Suggested Products fetched successfully.', 'data': json_data_product})

