from django.urls import path
from .views import*

urlpatterns = [

   path('', firstpage, name='firstpage'),
   path('log_out', log_out, name='log_out'),

#    path('index', index, name='index'),

    # user
    path('user_registration', user_registration, name='user_registration'),
    path('user_log', user_log, name='user_log'),
    path('user_home', user_home, name='user_home'),
    path('updateuser_profile/<int:pk>/', updateuser_profile, name='updateuser_profile'),
    # Add other URLs as needed

# caters
   
    path('cater_log', cater_log, name='cater_log'),
    path('cater_reg', cater_reg, name='cater_reg'),
    path('cater_home', cater_home, name='cater_home'),
    path('add_category/', add_category, name='add_category'),
    path('view_category', view_category, name='view_category'),
    path('delete_category/<int:id>/', delete_category, name='delete_category'),

    path('add_product', add_product, name='add_product'),
    path('view_produc', view_produc, name='view_produc'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('product/<int:product_id>/',view_product, name='view_product'),
    path('buy_now/<int:product_id>/', buy_now, name='buy_now'),

    path('requestform', requestform, name='requestform'),
    path('finished/<int:pk>/',finished, name='finished'),
    path('delete/<int:pk>/',delete, name='delete'),


    path('view_req', view_req, name='view_req'),
    path('update_profile/<int:pk>/', update_profile, name='update_profile'),
    

]

