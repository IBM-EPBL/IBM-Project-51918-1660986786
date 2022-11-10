def application_form(request):
 hide = Application.objects.filter(user=request.user)
 if request.method=="POST":
 form = ApplicationForm(request.POST, request.FILES)
 if form.is_valid():
 application = form.save()
 application.user = request.user
 application.save()
 return render(request, "application_form.html")
 else:
 form=ApplicationForm()
 return render(request, "application_form.html", { 'form':form,'hide':hide})
