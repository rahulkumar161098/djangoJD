from django.shortcuts import render, redirect
from django.http import HttpResponse
from leads.models import Lead, Agent
from leads.forms import CreateLead

# Create your views here.
def home_view(request):
   lead= Lead.objects.all()
   # context={
   #    lead: 'leads'
   # }
   return render(request, 'leads/home_page.html', {'lead':lead})

def lead_detail_view(request, id):
   details= Lead.objects.get(id=id)
   print(details)
   return render(request, 'leads/lead_detail_page.html', {'details':details})

def cerate_lead(request):
   form=CreateLead()
   if (request.method)=='POST':
      print('data received')
      form= CreateLead(request.POST)
      if form.is_valid():
         print('form valid')
         print(form.cleaned_data)
         first_name= form.cleaned_data['first_name']
         last_name= form.cleaned_data['last_name']
         age= form.cleaned_data['age']
         agent= Agent.objects.first()
         Lead.objects.create(first_name=first_name, last_name=last_name, age=age, agent=agent)
         return redirect('/leads')
      else:
         return render(request, 'leads/create_lead.html', context)
   context={
      'form': form
   }
   return render(request, 'leads/create_lead.html', context)
