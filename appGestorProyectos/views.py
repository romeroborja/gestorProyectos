from django.forms import model_to_dict
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View, TemplateView
from .forms import ProyectoForm, TareaForm, EmpleadoForm
from .models import Empleado, Proyecto, Tarea
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


# API
@method_decorator(csrf_exempt, name='dispatch')
class TareasAPI(View):

    def get(self, request):
        tareaList = Tarea.objects.all()
        return JsonResponse(list(tareaList.values()), safe=False)

    def post(self, request):
        tarea = Tarea()
        tarea.nombre = request.POST['nombre']
        tarea.descripcion = request.POST["descripcion"]
        tarea.fecha_inicio = request.POST["fecha_inicio"]
        tarea.fecha_fin = request.POST["fecha_fin"]
        tarea.responsable = Empleado.objects.get(pk=request.POST["responsable"])
        tarea.nivel_prioridad = request.POST["nivel_prioridad"]
        tarea.notas = request.POST["notas"]
        tarea.estado_tarea = request.POST["estado_tarea"]
        tarea.save()
        return JsonResponse(model_to_dict(tarea))


# HOME
class ProyectosListView(ListView):
    model = Proyecto
    template_name = 'home.html'
    queryset = Proyecto.objects.order_by('nombre')
    context_object_name = 'listado_proyectos'

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'TUS PROYECTOS'
        return context


# CLIENTE
class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = 'cliente.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del cliente'
        return context


# PROYECTOS
class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'

    def get_success_url(self):
        return reverse('proyecto_list')


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del proyecto'
        return context


class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('nombre')
    template_name = "proyecto_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de proyectos'
        return context


class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = "proyecto_delete.html"
    success_url = reverse_lazy('proyecto_list')


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyecto_update.html"
    success_url = reverse_lazy('proyecto_list')


# TAREAS
class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_formJS.html'

    def get_success_url(self):
        return reverse('tarea_list')


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la tarea'
        return context


class TareasListView(TemplateView):
    template_name = 'tarea_listJS.html'


class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "tarea_delete.html"
    success_url = reverse_lazy('tareas_list')


class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "tarea_update.html"
    success_url = reverse_lazy('tarea_list')


# EMPLEADOS
class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'

    def get_success_url(self):
        return reverse('empleado_list')


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalle del empleado'
        return context


class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('nombre')
    template_name = "empleado_list.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de empleados'
        return context


class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = "empleado_delete.html"
    success_url = reverse_lazy('empleado_list')


class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado_update.html"
    success_url = reverse_lazy('empleado_list')
