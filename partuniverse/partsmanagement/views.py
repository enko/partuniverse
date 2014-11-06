from django.views.generic.base import View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
# Class based views to create a new dataset and Update one
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Current time
from django.utils.timezone import now

# Importing models
from partsmanagement.models import Part
from partsmanagement.models import Transaction

class PartsList(ListView):
	model = Part
	template_name = 'pmgmt/list.html'

class TransactionListView(ListView):
	model = Transaction
	template_name = 'pmgmt/trans_list.html'

class PartsAddView(CreateView):
	model = Part
	success_url='/'
	template_name='pmgmt/add.html'
	fields = (	'name',
				'min_stock',
				'on_stock',
				'unit',
				'manufacturer',
				'distributor',
				'categories' )

	def form_valid(self, form):
		user = self.request.user
		form.instance.created_by = user
		form.instance.timestamp = now()
		return super(PartsAddView, self).form_valid(form)

class PartDeleteView(DeleteView):
	model = Part
	success_url = reverse_lazy('partslist')
	template_name = 'pmgmt/delete.html'

class PartDetailView(DetailView):
	template_name = "pmgmt/detail.html"
	model = Part

class PartUpdateView(UpdateView):
	template_name = "pmgmt/update.html"
	success_url = reverse_lazy('partslist')
	model = Part
	# We don't want to amke all fields editable via
	# normal frontend.
	fields = (	'name',
				'min_stock',
				'unit',
				'manufacturer',
				'distributor',
				'categories' )

class TransactionAddView(CreateView):

	model = Transaction
	success_url='/'
	template_name='pmgmt/add.html'
	fields = (	'subject',
				'part',
				'amount',
				'comment')

	def form_valid(self, form):
		user = self.request.user
		form.instance.created_by = user
		form.instance.timestamp = now()
		return super(TransactionAddView, self).form_valid(form)

