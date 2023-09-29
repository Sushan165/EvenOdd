from django.shortcuts import render, redirect

def pnf(request,exception):
	return redirect("home")

def home(request):
	if request.method == "POST":
		num = int(request.POST.get("num"))
		if num % 2 == 0:
			msg = "num " + str(num) + " is Even"
		else:
			msg = "num " +str(num) + " is Odd"
		return render(request,"home.html",{"msg":msg})
	else:
		return render(request,"home.html")
