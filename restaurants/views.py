from django.shortcuts import render

# Create your views here.
def coded(request):
	context = {
		"msg" : "Hello World!"
	}

	return render(request, 'bootcamp.html', context)