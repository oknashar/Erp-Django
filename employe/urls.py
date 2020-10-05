from django.urls import path

from . import views

app_name = 'employe'

urlpatterns = [
   path('',views.Employe_list,name ='getEmploye'),
   path('absense',views.Absense_list,name ='getAbsense'),
   path('absense/day',views.AbsenseDay_list,name ='getDayAbsense'),
   path('delete/<int:id>',views.delete_Employe,name ='deleteEmploye'),
   path('add',views.addEmploye,name ='addEmploye'),
   path('update/<int:id>',views.edit_Employe,name ='editEmploye'),
   path('signin/<int:id>',views.SignIn,name ='signInAbsense'),
   path('signout/<int:id>',views.Signout,name ='signOutAbsense'),
]


 