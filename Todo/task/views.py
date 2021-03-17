from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,CustomerForm,TaskForm,NoteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer,Task,Note
# Create your views here.

@login_required(login_url='login')
def customer_view(request, customer_id):
	try:
		ID = int(customer_id)
		if Customer.objects.filter(id = ID, added_by = request.user).exists():
			context = {
				"my_customer": Customer.objects.get(id = ID)
			}
			return render(request, "task/customer.html", context)
		else:
			return redirect("home page")
	except:
		return redirect("home page")



@login_required(login_url='login')
def index(request):
	form=CustomerForm()
	customers=Customer.objects.filter(added_by = request.user)
	
	if request.method=='POST':

		new_customer = Customer(
			first_name = request.POST['first_name'], 
			last_name = request.POST['last_name'],
			email = request.POST['email'],
			added_by = request.user
		)

		new_customer.save()
		return redirect('home page')
		
			
	return render(request,'task/index.html',{'form':form,'customers':customers})


def delete_items(request, pk):
	data = Customer.objects.get(id=pk)
	if request.method == 'POST':
		data.delete()
		# messages.success(request,'successfully deleted')
		return redirect('home page')
	return render(request, 'task/task_confirm_delete.html')





def register(request):


	form=UserRegistrationForm()

	if request.method=='POST':

		form=UserRegistrationForm(request.POST)

		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created, Login now')

			return redirect('login')
		
			
	return render(request,'task/register.html',{'form':form})   



def task(request):
	tasks=Task.objects.all()
	form=TaskForm()
	if request.method=='POST':
		form=TaskForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('task')

	return render(request,'task/task.html',{'form':form,'tasks':tasks})





def update(request,id):
    
    if request.method=='POST':
        data=Task.objects.get(pk=id)
        fm=TaskForm(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('task')
    else:
        data=Task.objects.get(pk=id)
        fm=TaskForm(instance=data)   
      
    return render(request,'task/edit.html',{"form":fm})



def delete(request, pk):
	data = Task.objects.get(id=pk)
	if request.method == 'POST':
		data.delete()
		# messages.success(request,'successfully deleted')
		return redirect('task')
	return render(request, 'task/delete.html')




def note(request):
	notes=Note.objects.all()
	form=NoteForm()
	if request.method=='POST':

		form=NoteForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('note')

	return render(request,'task/note.html',{'form':form,'notes':notes})



def update_note(request,id):
    
    if request.method=='POST':
        data=Note.objects.get(id=id)
        fm=NoteForm(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('note')
    else:
        data=Note.objects.get(id=id)
        fm=NoteForm(instance=data)   
      
    return render(request,'task/note_edit.html',{"form":fm})



def delete_note(request, id):
	data = Note.objects.get(id=id)
	if request.method == 'POST':
		data.delete()
		# messages.success(request,'successfully deleted')
		return redirect('note')
	return render(request, 'task/note_delete.html')



	