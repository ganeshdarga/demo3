from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

from rest_framework import status


import datetime
from rest_framework.decorators import action
from api.models import activities,admin,companies,invoice,leads,prequest,tasks,ticket,user,usercheck,usernotification
from api.serializers import activitiesSerializers,adminSerializers,companiesSerializers,invoiceSerializers,leadsSerializers,prequestSerializers,tasksSerializers,ticketSerializers,userSerializers,usercheckSerializers,usernotificationSerializers

# Create your views here.

class activitiesViewSet(viewsets.ModelViewSet):
    queryset = activities.objects.all()
    serializer_class = activitiesSerializers

    @action(detail=False, methods=['post'])
    def addactivity(self,request):
        addDate =  request.data.get("addDate")
        addDay =  request.data.get("addDay")
        addStarttime =  request.data.get("addStarttime")
        addEndtime =  request.data.get("addEndtime")
        addDis =  request.data.get("addDis")
        try:
            new_request = activities.objects.create(dates=addDate,days=addDay,starttime=addStarttime,endtime=addEndtime,Discription=addDis)
            serializer = activitiesSerializers(new_request, context={'request':request})
            return Response(activitiesSerializers(new_request).data, status=201)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to set data'}, status=400)

    @action(detail=False, methods=['post'])
    def editactivity(self,request):
        activity_id = request.query_params.get("id")
        addDate =  request.data.get("addDate")
        addDay =  request.data.get("addDay")
        addStarttime =  request.data.get("addStarttime")
        addEndtime =  request.data.get("addEndtime")
        addDis =  request.data.get("addDis")
        try:
            activity_instance = activities.objects.get(id=activity_id)
            activity_instance.dates = addDate
            activity_instance.days = addDay
            activity_instance.starttime = addStarttime
            activity_instance.endtime = addEndtime
            activity_instance.Discription =  addDis
            activity_instance.save()
            serializer = activitiesSerializers(activity_instance, context={'request': request})
            return Response(serializer.data, status=200)
        except activities.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to edit data'}, status=400)
    
    @action(detail=False , methods=['delete'])
    def deleteactivity(self,request):
        activity_id = request.data.get("deleteId")
        print(activity_id)
        try:
            activity_instance = activities.objects.get(id = activity_id)
            print(activity_instance)
            activity_instance.delete()
            serializer = activitiesSerializers(activity_instance, context={'request': request})
            return Response({'message': 'invoice deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except activities.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to delete task'}, status=status.HTTP_400_BAD_REQUEST)


class adminViewSet(viewsets.ModelViewSet):
    queryset = admin.objects.all()
    serializer_class = adminSerializers

    @action(detail=False, methods=['get'])
    def login(self, request):
        name = request.data.get('adminname')
        password = request.data.get('adminpassword')
        print(name)
        print(password)
        try:
            admin = Admin.objects.get(name=name, password=password)
            return Response(AdminSerializer(admin).data)
        except Admin.DoesNotExist:
            return Response({'message': 'wrong details'}, status=400)

class companiesViewSet(viewsets.ModelViewSet):
    queryset = companies.objects.all()
    serializer_class = companiesSerializers

    @action(detail=False, methods=['post'])
    def addcompany(self,request):
        companyname = request.data.get("companyname")
        companyemail = request.data.get("companyemail")
        comapanymobile = request.data.get("comapanymobile")
        companymanage = request.data.get("companymanage")
        companystatus = request.data.get("companystatus")
        try:
            new_request = companies.objects.create(companyName=companyname,Email=companyemail,mobile=comapanymobile,manage=companymanage,statuss=companystatus)
            serializer = companiesSerializers(new_request, context={'request': request})
            return Response(companiesSerializers(new_request).data, status=201)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to set data'}, status=400)

    @action(detail=False,methods=['post'])
    def subcompanyedit(self,request):
        company_id = request.query_params.get("id")
        companyname = request.data.get("companyname")
        companyemail = request.data.get("companyemail")
        comapanymobile = request.data.get("comapanymobile")
        companymanage = request.data.get("companymanage")
        companystatus = request.data.get("companystatus")

        try:
            company_instance = companies.objects.get(id=company_id)
            company_instance.companyName = companyname
            company_instance.Email = companyemail
            company_instance.mobile = comapanymobile
            company_instance.manage=companymanage
            company_instance.statuss = companystatus
            company_instance.save()
            serializer = companiesSerializers(company_instance, context={'request': request})
            return Response(serializer.data, status=200)
        except companies.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to edit data'}, status=400)

    @action(detail=False , methods=['delete'])
    def detetecompanydata(self,request):
        comapny_id = request.data.get("deleteId")
        print(comapny_id)
        try:
            company_instance = companies.objects.get(id = comapny_id)
            print(company_instance)
            company_instance.delete()
            serializer = companiesSerializers(company_instance, context={'request': request})
            return Response({'message': 'invoice deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except companies.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Unable to delete task'}, status=status.HTTP_400_BAD_REQUEST)



class invoiceViewSet(viewsets.ModelViewSet):
    queryset = invoice.objects.all()
    serializer_class = invoiceSerializers

    @action(detail=False, methods=['post'])
    def addinvoice(self,request):
        accountnumber = request.data.get("accountnumber")
        account = request.data.get("account")
        amount = request.data.get("amount")
        invoicedate = request.data.get("invoicedate")
        duedate = request.data.get("duedate")
        type = request.data.get("type")
        status = request.data.get("status")
        try:
            new_request = invoice.objects.create(accountNumber=accountnumber,account=account,Amount=amount,invoiceDate=invoicedate,dueDate=duedate,type=type,status=status)
            serializer = invoiceSerializers(new_request, context={'request': request})
            return Response(invoiceSerializers(new_request).data, status=201)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to set data'}, status=400)

    @action(detail=False,methods=['post'])
    def subinvoiceedit(self,request):
        invoie_id = request.query_params.get("id")
        accountnumber = request.data.get("accountnumber")
        account = request.data.get("account")
        amount = request.data.get("amount")
        invoicedate = request.data.get("invoicedate")
        duedate = request.data.get("duedate")
        type = request.data.get("type")
        status = request.data.get("status")

        try:
            invoice_instance = invoice.objects.get(id=invoie_id)
            invoice_instance.accountNumber = accountnumber
            invoice_instance.account = account
            invoice_instance.Amount = amount
            invoice_instance.invoiceDate = invoicedate
            invoice_instance.dueDate = duedate
            invoice_instance.type = type
            invoice_instance.status=status
            invoice_instance.save()
            serializer = invoiceSerializers(invoice_instance, context={'request': request})
            return Response(serializer.data, status=200)
        except invoice.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to edit data'}, status=400)

    @action(detail=False , methods=['delete'])
    def deleteinvoice(self,request):
        invoice_id = request.data.get("deleteId")
        print(invoice_id)
        try:
            invoice_instance = invoice.objects.get(id = invoice_id)
            print(invoice_instance)
            invoice_instance.delete()
            serializer = invoiceSerializers(invoice_instance, context={'request': request})
            return Response({'message': 'invoice deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except invoice.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Unable to delete task'}, status=status.HTTP_400_BAD_REQUEST)



class leadsViewSet(viewsets.ModelViewSet):
    queryset = leads.objects.all()
    serializer_class = leadsSerializers

    @action(detail=False, methods=['post'])
    def addleads(self,request):
        leadname = request.data.get("leadname")
        leadtitle = request.data.get("leadtitle")
        leadcompany = request.data.get("leadcompany")
        leadphone = request.data.get("leadphone")
        leademail = request.data.get("leademail")
        lead_status = request.data.get("lead_status")
        leadcreate = request.data.get("leadcreate")
        leadowner = request.data.get("leadowner")
        try:
            new_request = leads.objects.create(Name=leadname,Title=leadtitle,company=leadcompany,phone=leadphone,email=leademail,lead_status=lead_status,Lead_created=leadcreate,Lead_owner=leadowner)
            serializer = leadsSerializers(new_request, context={'request': request})
            return Response(leadsSerializers(new_request).data, status=201)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to set data'}, status=400)

    @action(detail=False,methods=['post'])
    def leadedit(self,request):
        lead_id = request.query_params.get("id")
        leadname = request.data.get("leadname")
        leadtitle = request.data.get("leadtitle")
        leadcompany = request.data.get("leadcompany")
        leadphone = request.data.get("leadphone")
        leademail = request.data.get("leademail")
        lead_status = request.data.get("lead_status")
        leadcreate = request.data.get("leadcreate")
        leadowner = request.data.get("leadowner")
        print(lead_id)

        try:
            lead_instance = leads.objects.get(id=lead_id)
            lead_instance.Name = leadname
            lead_instance.Title = leadtitle
            lead_instance.company=leadcompany
            lead_instance.phone = leadphone
            lead_instance.email = leademail
            lead_instance.lead_status = lead_status
            lead_instance.Lead_created=leadcreate
            lead_instance.Lead_owner = leadowner
            lead_instance.save()
            serializer = leadsSerializers(lead_instance, context={'request': request})
            return Response(serializer.data, status=200)
        except leads.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to edit data'}, status=400)

    @action(detail=False , methods=['delete'])
    def deteteleaddata(self,request):
        lead_id = request.data.get("deleteId")
        print(lead_id)
        try:
            lead_instance = leads.objects.get(id = lead_id)
            print(lead_instance)
            lead_instance.delete()
            serializer = leadsSerializers(lead_instance, context={'request': request})
            return Response({'message': 'invoice deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except leads.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to delete task'}, status=status.HTTP_400_BAD_REQUEST)
    



class prequestViewSet(viewsets.ModelViewSet):
    queryset = prequest.objects.all()
    serializer_class = prequestSerializers

    @action(detail=False, methods=['post'])
    def submit_request(self, request):
        name = request.data.get('serviseUser')
        email = request.data.get('serviceEmail')
        contactno = request.data.get('serviceContact')
        company = request.data.get('serviceCompany')
        services = request.data.get('serviceMessage')
        query = request.data.get('typesofservices')
        status=0
        others="cgf"
        remark=1
        posting_date = datetime.datetime.now().date() 
        print(name)
        try:
            new_request = prequest.objects.create(name=name,email=email,contactno=contactno,company=company,services=services,query=query,status=status,posting_date=posting_date,others=others,remark=remark)
            serializer = prequestSerializers(new_request, context={'request': request})
            return Response(prequestSerializers(new_request).data, status=201)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to set data'}, status=400)

    @action(detail=False,methods=['get'])
    def getiddata(self,request):
        quote_id = request.query_params.get("id")
        print(quote_id)
        if not quote_id:
            return Response({"message": "ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = prequest.objects.get(id=quote_id)
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except prequest.DoesNotExist:
            return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to add data'}, status=400)

class tasksViewSet(viewsets.ModelViewSet):
    queryset = tasks.objects.all()
    serializer_class = tasksSerializers

    @action(detail=False, methods=['post'])
    def addtask(self,request):
        taskname =  request.data.get("taskname")
        deadline =  request.data.get("deadline")
        taskstatus =  request.data.get("taskstatus")
        taskassignee =  request.data.get("taskassignee")

        try:
            new_request =  tasks.objects.create(Taskname=taskname,deadLine=deadline,status=taskstatus,Asignee=taskassignee)
            serializer = tasksSerializers(new_request, context={"request":request})
            return Response(tasksSerializers(new_request).data, status=201)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to add data'}, status=400)

    @action(detail=False , methods=['post'])
    def edittask(self,request):
        task_id = request.query_params.get("id")
        taskname =  request.data.get("taskname")
        deadline =  request.data.get("deadline")
        taskstatus =  request.data.get("taskstatus")
        taskassignee =  request.data.get("taskassignee")
        print(task_id)
        try:
             user_instance = tasks.objects.get(id=task_id)
             user_instance.Taskname = taskname
             user_instance.deadLine = deadline
             user_instance.status = taskstatus
             user_instance.Asignee = taskassignee
             user_instance.save()
             serializer = tasksSerializers(user_instance, context={'request': request})
             return Response(serializer.data, status=200)
        except tasks.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to edit data'}, status=400)

    @action(detail=False , methods=['delete'])
    def deletetask(self,request):
        task_id = request.data.get("Id1")
        print(task_id)
        try:
            task_instance = tasks.objects.get(id = task_id)
            print(task_instance)
            task_instance.delete()
            serializer = tasksSerializers(task_instance, context={'request': request})
            return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except tasks.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Unable to delete task'}, status=status.HTTP_400_BAD_REQUEST)

        

class ticketViewSet(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = ticketSerializers

    @action(detail=False, methods=['post'])
    def create_ticket(self,request):
        UserName = request.data.get("UserName")
        subject = request.data.get("subject")
        tasktype = request.data.get("tasktype")
        Prioritys = request.data.get("Prioritys")
        Discriptions = request.data.get("Discriptions")
        Emails = request.data.get("Emails")
        status = "active"
        adminremark = "pending"
        posting_date = datetime.datetime.now().date()
        admin_remark_date = datetime.datetime.now()
        try:
            new_request = ticket.objects.create(User_Name=UserName,email_id=Emails,subject=subject,task_type=tasktype,prioprity=Prioritys,ticket=Discriptions,status=status,posting_date=posting_date,admin_remark=adminremark)
            serializer = ticketSerializers(new_request, context={'request': request})
            return Response(ticketSerializers(new_request).data, status=201)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to set data'}, status=400)

    @action(detail=False, methods=['get'])
    def view_ticket(self, request):
        print("Received query parameters:", request.query_params)
        email = request.query_params.get('userEmail')
        print(email)
        if not email:
            return Response({'message': 'Email parameter is required'}, status=400)
        try:
            # Use filter to get all matching tickets
            tickets = ticket.objects.filter(email_id=email)
            if tickets.exists():
                serializer = ticketSerializers(tickets, many=True, context={'request': request})
                return Response(serializer.data)
            else:
                return Response({'message': 'No tickets found for this email'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'An error occurred'}, status=500)

    @action(detail=False, methods=['post'])
    def setupdatestatus(self,request):
        ticket_id = request.query_params.get("id")
        textarea = request.data.get("textarea")
        status = "closed"
        try:
            ticket_instance = ticket.objects.get(id=ticket_id)
            print(ticket_instance)
            ticket_instance.admin_remark = textarea
            ticket_instance.status = status
            ticket_instance.save()
            
            # Serialize and return the updated user data
            serializer = ticketSerializers(ticket_instance, context={'request': request})
            return Response(serializer.data, status=200)
        except ticket.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
           
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to set data'}, status=400)


    


class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializers


    @action(detail=False, methods=['post'])
    def setuserEdit(self, request):
        print("Received query parameters:", request.query_params)
        user_id = request.query_params.get('userEmail')
        Username = request.data.get("userName")
        userEmail = request.data.get("userEmail_id")
        useAlterEmail = request.data.get("useAlterEmail")
        userMobile = request.data.get("userMobile")
        UserGender = request.data.get("UserGender")
        userAddress = request.data.get("userAddress")
        print(user_id)
        print(Username)
        try:
            # Fetch the user object based on the provided id
            user_instance = user.objects.get(email=user_id)
            print(user_id)
            
            # Update fields of the user instance
            user_instance.name = Username
            user_instance.email = userEmail
            user_instance.alt_email = useAlterEmail
            user_instance.mobile = userMobile
            user_instance.gender = UserGender
            user_instance.address = userAddress
            
            # Save the updated user instance
            user_instance.save()
            
            # Serialize and return the updated user data
            serializer = userSerializers(user_instance, context={'request': request})
            return Response(serializer.data, status=200)
        except user.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
           
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to set data'}, status=400)

    @action(detail=False, methods=['post'])
    def changepassword(self,request):
        userEmail = request.data.get("userEmail")
        currentpassword =  request.data.get("currentpassword")
        newpassword = request.data.get("newpassword")
        print("Request Data:", request.data)
        try:
            user_instance = user.objects.get(email=userEmail)
            print(user_instance.password)
            if (currentpassword == user_instance.password):
                user_instance.password = newpassword
                user_instance.save()
                print(user_instance.password)
                serializer = userSerializers(user_instance, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Current password is incorrect'}, status=400)
        
        except user.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        
        except Exception as e:
            print(f"Error: {e}")
            return Response({'message': 'Unable to change password'}, status=400)


    @action(detail=False, methods=['get'])
    def login(self, request):
        email = request.data.get('useremail')
        password = request.data.get('userpassword')
        try:
            user = User.objects.get(email=email, password=password)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response({'message': 'Incorrect Email or Password'}, status=400)

    @action(detail=False, methods=['get'])
    def viewUser(self, request):
        print("Received query parameters:", request.query_params)
        email = request.query_params.get('userEmail')
        print(email)
        if not email:
            return Response({'message': 'Email parameter is required'}, status=400)
        try:
            # Use filter to get all matching tickets
            users = user.objects.filter(email=email)
            if users.exists():
                serializer = userSerializers(users, many=True, context={'request': request})
                return Response(serializer.data)
            else:
                return Response({'message': 'No tickets found for this email'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'An error occurred'}, status=500)


    @action(detail=False , methods=['post'])
    def submitedit(self,request):
        user_id = request.query_params.get("Id")
        Username =  request.data.get("Username")
        userEmail =  request.data.get("userEmail")
        useAlterEmail =  request.data.get("useAlterEmail")
        userMobile =  request.data.get("userMobile")
        UserGender = request.data.get("UserGender")
        userAddress = request.data.get("userAddress")
        userPassword = request.data.get("userPassword")
        print(user_id)
        try:
             user_instance = user.objects.get(id=user_id)
             user_instance.name = Username
             user_instance.email = userEmail
             user_instance.alt_email = useAlterEmail
             user_instance.mobile = userMobile
             user_instance.gender =UserGender
             user_instance.address = userAddress
             user_instance.password =userPassword
             user_instance.save()
             serializer = userSerializers(user_instance, context={'request': request})
             return Response(serializer.data, status=200)
        except user.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'Unable to edit data'}, status=400)

    @action(detail=False , methods=['delete'])
    def submitdelete(self,request):
        user_id = request.data.get("Id1")
        print(user_id)
        try:
            user_instance = user.objects.get(id = user_id)
            print(user_instance)
            user_instance.delete()
            serializer = userSerializers(user_instance, context={'request': request})
            return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except user.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Unable to delete task'}, status=status.HTTP_400_BAD_REQUEST)
            

class usercheckViewSet(viewsets.ModelViewSet):
    queryset = usercheck.objects.all()
    serializer_class = usercheckSerializers

class usernotificationViewSet(viewsets.ModelViewSet):
    queryset = usernotification.objects.all()
    serializer_class = usernotificationSerializers