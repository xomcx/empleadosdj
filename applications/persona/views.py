from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
#models
from .models import Empleado
#forms
from .forms import EmpleadoForm

#Carga la pagina de Inicio
class InicioView(TemplateView):
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
# Create your views here.
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista


class ListByAreaEmpleado(ListView):
    """ lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(departamento__shor_name=area)
        return lista


class ListByTrabajoEmpleado(ListView):
    """ lista empleados por trabajo """
    template_name = 'persona/list_by_trabajo.html'

    def get_queryset(self):
        trabajo = self.kwargs['trabajo']
        lista = Empleado.objects.filter(job=trabajo)
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


class ListEmpleadosByKword(ListView):
    """ lista empleado por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        if palabra_clave == '':
            palabra_clave = 1
        else:
            palabra_clave = palabra_clave           
        empleado = Empleado.objects.get(id=palabra_clave)
        habilidades = empleado.habilidades.all()
        return habilidades

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # Todo un proceso
        context['titulo'] = 'Empleado del mes' 
        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')
        
    #funcion para verificar la valides del form y concatenar 2 modelos
    #como nombre y apellidos       
    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = ['first_name','last_name','job','departamento','habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('****************METHOD POST***************')
        print('-------------------------------')
        print('*******************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)    

    def form_valid(self, form):
        print('****************METHOD FORM_VALID***************')
        print('*******************************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')
        