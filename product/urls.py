from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
   path('color',views.color_list,name ='getColor'),
   path('color/add',views.addColor,name ='addColor'),
   path('color/edit/<int:id>',views.edit_Color,name ='editColor'),
   path('color/delete/<int:id>',views.delete_Color,name ='deleteColor'),

   path('category',views.Category_list,name ='getCategory'),
   path('category/add',views.addCategory,name ='addCategory'),
   path('category/edit/<int:id>',views.edit_Category,name ='editCategory'),
   path('category/delete/<int:id>',views.delete_Category,name ='deleteCategory'),
   
   path('type',views.Type_list,name ='getType'),
   path('type/add',views.addType,name ='addType'),
   path('type/edit/<int:id>',views.edit_Type,name ='editType'),
   path('type/delete/<int:id>',views.delete_Type,name ='deleteType'),

   path('creator',views.Creator_list,name ='getCreator'),
   path('creator/add',views.addCreator,name ='addCreator'),
   path('creator/edit/<int:id>',views.edit_creator,name ='editCreator'),
   path('creator/delete/<int:id>',views.delete_creator,name ='deleteCreator'),
   
   
   path('product',views.Product_list,name ='getProduct'),
   path('product/add',views.addProduct,name ='addProduct'),
   path('product/edit/<int:id>',views.edit_Product,name ='editProduct'),
   path('product/delete/<int:id>',views.delete_Product,name ='deleteProduct'),

   path('product/addtocart/<slug:barcode>',views.add_to_cart,name ='addToCart'),
   path('product/removefromcart/<slug:barcode>',views.remove_from_cart,name ='removeFromCart'),
   path('product/removeproductfromcart/<slug:barcode>',views.remove_Product_from_cart,name ='removeProductFromCart'),

   path('product/removeproductfromorder/<slug:barcode>/<int:id>',views.remove_Product_from_order,name ='removeProductfromOrder'),

   path('product/ordersummery',views.OrderSummery.as_view(),name ='orderSummery'),
   
   path('product/addempfororder/<int:id>',views.updateOrder,name ='updateSummery'),

   path('product/checkout',views.checkOut,name ='checkout'),

   path('product/getOrders',views.getOrders,name ='Orders'),
   path('product/getDayOrders',views.getDayOrders,name ='DayOrders'),

   path('product/addProducttoCart',views.getDataAndPushInOrder,name ='addtoCart'),

]
