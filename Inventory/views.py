from rest_framework.views import APIView    #class based views
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class ProductView(APIView): 
    def get(self,request):
        all_products=Product.objects.all()
    #     products_data=[]
    #     for product in all_products:
    #         single_product={
    #             'id':product.id,
    #             'product_name':product.product_name,
    #             'code':product.code,
    #             'price':product.price
    #             }
    #         products_data.append(single_product)
        serialized_products=Products_serializers2(all_products,many=True).data

        return Response(serialized_products)


    def post(self,request):
        #print(request.data) 
        new_product=Product(product_name=request.data["product_name"],code=request.data["code"],price=request.data["price"])
        new_product.save()
        return Response('Data Saved')
    
#How to get a individual data by using ID
class ProductViewById(APIView):
    def get(self,request,id):
        product=Product.objects.get(id=id)   
    
        # single_product={
        #         'id':product.id,
        #         'product_name':product.product_name,
        #         'code':product.code,
        #         'price':product.price
        #         }
    
        single_product=Products_serializers(product).data

        return Response(single_product) 
    
    def patch(self,request,id):
        product=Product.objects.filter(id=id) 

        product.update(product_name=request.data["product_name"],code=request.data["code"],price=request.data["price"])

        return Response('Updated')

    def delete(self,request,id):
        product=Product.objects.get(id=id) 

        product.delete()

        return Response('Deleted')