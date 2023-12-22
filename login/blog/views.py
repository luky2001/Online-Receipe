from django.shortcuts import render,redirect
from django.contrib.auth.forms import User
#from django.contrib.auth import login,logout 
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required




def home(request):
	return render(request, 'base.html')




@login_required(login_url="/login/")
def receipe(request):
	if request.method=="POST":
	
		data = request.POST
		image = request.FILES.get('image')
		name=data.get('name')
		disc = data.get('disc')
	
		

		Receipe.objects.create(
			receipe_image = image,
			receipe_name=name,
			receipe_discription = disc,


			)
		return redirect("/receipe/")
		

	queryset = Receipe.objects.all()
	if request.GET.get('search'):
		queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))


	context = {'receipe':queryset}
	
	return render(request,'index.html',context)






def update(request,id):
	print("id==",id)
	queryset = Receipe.objects.get(id=id)
	if request.method=="POST":
		print("here data==",queryset.__dict__)
		#data = request.POST 
		data = request.POST
		print("latest data==",data)
		image = request.POST.get('image')
		name=data.get('name')
		disc = data.get('disc')
		print("latest data==",name,disc,image)
		queryset.receipe_name= name 
		queryset.receipe_discription = disc
		if image:
			queryset.receipe_image= image
		 

		queryset.save()
		print(queryset.receipe_name)
		return redirect("/receipe/")

		
	context = {'receipe':queryset}
	return render(request,'update.html',context)







	







def delete(request,id):
	queryset = Receipe.objects.get(id=id)
	queryset.delete()
	return redirect('/receipe')



def login_page(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')

		if not User.objects.filter(username=username).exists():
			messages.error(request, "Invalid Username")
			return redirect("/login/")
		user =authenticate(username=username,password=password)
		if user is None:
			messages.error(request,"Invalid Password")
			return redirect('/login/')
		else:
			login(request,user)
			return redirect("/receipe/")


	return render(request,'login.html')

def logout_page(request):
	logout(request)
	return redirect('/login/')


def register(request):
	if request.method=="POST":
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		username=request.POST.get('username')
		password=request.POST.get('password')
		#first_name=request.POST.get('firast_name')

		user = User.objects.filter(username=username)
		if user.exists():
			messages.info(request,'username already register')
			return  redirect('/register/')

		user = User.objects.create(
			first_name = first_name,
			last_name = last_name,
			username = username,
			#password = password
			)
		user.set_password(password)
		user.save()
		messages.info(request,"Account created successfully")

		return redirect('/register')



	return render(request,'register.html')



