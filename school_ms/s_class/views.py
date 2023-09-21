
from django.shortcuts import render, redirect
from .forms import SectionForm
from classes.models import SchoolClasses
from .models import Section_class

def create_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.save()  # Save the section first without the class_name relationship

            # Add the selected classes to the section
            for class_name in request.POST.getlist('class_name'):
                section.class_name.add(class_name)

            form.save_m2m()  # Save the many-to-many relationships

            return redirect('class_list')  # Redirect to a success page or another URL
    else:
        form = SectionForm()
    
    return render(request, 'section_form.html', {'form': form})


def class_section_count(request):
    # Fetch all classes
    classes = SchoolClasses.objects.all()

    # Create a dictionary to store class-wise section details and counts
    class_counts = {}

    # Calculate section counts and details for each class
    for class_obj in classes:
        sections = Section_class.objects.filter(class_name=class_obj)
        section_details = [section.section_name for section in sections]
        section_count = len(sections)
        class_counts[class_obj] = {
            'sections': section_details,
            'section_count': section_count,
        }

    return render(request, 'class_section_count.html', {'class_counts': class_counts})



