from django.contrib import admin
from django.urls import path,include

from api.views import activitiesViewSet,adminViewSet,companiesViewSet,invoiceViewSet,leadsViewSet,prequestViewSet,tasksViewSet,ticketViewSet,userViewSet,usercheckViewSet,usernotificationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'activities',activitiesViewSet)
router.register(r'admin',adminViewSet)
router.register(r'companies',companiesViewSet)
router.register(r'invoice',invoiceViewSet)
router.register(r'leads',leadsViewSet)
router.register(r'prequest',prequestViewSet)
router.register(r'tasks',tasksViewSet)
router.register(r'ticket',ticketViewSet)
router.register(r'user',userViewSet)
router.register(r'usercheck',usercheckViewSet)
router.register(r'usernotification',usernotificationViewSet)

urlpatterns = [
    path('',include(router.urls))
]
