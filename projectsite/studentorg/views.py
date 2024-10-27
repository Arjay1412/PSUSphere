from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember
from studentorg.forms import OrganizationForm, OrgMemberForm
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class Organizationlist(ListView):
    model = Organization
    content_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberlist(ListView):
    model = OrgMember
    content_object_name = 'organization'
    template_name = 'orgmember_list.html'
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')
