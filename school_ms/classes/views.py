from django.shortcuts import render, redirect, get_object_or_404
from .models import SchoolClasses
from .forms import SchoolClassesForm

def class_list(request):
    classes = SchoolClasses.objects.all()
    return render(request, 'class_list.html',{'classes': classes})

def add_class(request):
    if request.method == 'POST':
        form = SchoolClassesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = SchoolClassesForm()
    
    return render(request, 'add_class.html', {'form': form})

def edit_class(request, class_name):
    instance = get_object_or_404(SchoolClasses, class_name=class_name)
    
    if request.method == 'POST':
        form = SchoolClassesForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = SchoolClassesForm(instance=instance)
    
    return render(request, 'edit_class.html', {'form': form, 'instance': instance})

def delete_class(request, class_name):
    
    class_obj = get_object_or_404(SchoolClasses, class_name=str(class_name)) 
    print(class_obj)
    
    if request.method == 'POST':
        class_obj.delete()
        return redirect('class_list')
    
    return render(request, 'delete_class.html', {'class_obj': class_obj})

