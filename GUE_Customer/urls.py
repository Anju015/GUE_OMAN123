from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    # path("emp",views.reg),
#customer feedback...
     path("feedback",views.customer_feedback),
     path("custreg",views.customer_registration),
     path("viewcustomer",views.viewcust),
]