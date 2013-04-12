# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from models import *

@csrf_exempt
def energy_file( request ):

   if request.method=='GET':
   	print "I rock"
   if request.method=='POST':
   	print "I posr"


   Energy_Data_File = EnergyData()

   FileContent = ContentFile(request.FILES['Data'].read())
   FileName = request.FILES['Data'].name
   print FileName
   #print FileContent,type(FileContent)
   #print "\n",request.FILES['Data'].read()
   Energy_Data_File.FILE.save(FileName, FileContent)
   
   Energy_Data_File.save()
       
   return HttpResponse()
# Create your views here.
