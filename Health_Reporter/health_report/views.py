from django.shortcuts import render

from django.http import Http404
import os
import socket
def home(request):
	hostname = socket.gethostname()    
	IPAddr = socket.gethostbyname(hostname) 
	return render(request,'home.html',{
		'hostname':hostname,
		'ip':IPAddr
	})
