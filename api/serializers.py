
from rest_framework import serializers

from api.models import activities,admin,companies,invoice,leads,prequest,tasks,ticket,user,usercheck,usernotification
#create serilizers

class activitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model=activities
        fields ="__all__"

class adminSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=admin
        fields ="__all__"

class companiesSerializers(serializers.ModelSerializer):
    class Meta:
        model=companies
        fields ="__all__"
class invoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model=invoice
        fields ="__all__"

class leadsSerializers(serializers.ModelSerializer):
    class Meta:
        model=leads
        fields ="__all__"
class prequestSerializers(serializers.ModelSerializer):
    class Meta:
        model=prequest
        fields ="__all__"

class tasksSerializers(serializers.ModelSerializer):
    class Meta:
        model=tasks
        fields ="__all__"

class ticketSerializers(serializers.ModelSerializer):
    class Meta:
        model=ticket
        fields ="__all__"
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=user
        fields ="__all__"
class usercheckSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=usercheck
        fields ="__all__"

class usernotificationSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=usernotification
        fields ="__all__"