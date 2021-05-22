from django.urls import path
from . import views

urlpatterns = [
    # API
    path('tareasAPI/', views.TareasAPI.as_view(), name='tareasAPI'),
    # HOME
    path('', views.ProyectosListView.as_view(), name='home'),
    # PROYECTOS
    path('nuevo_proyecto/', views.ProyectoCreateView.as_view(), name='proyecto_form'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('proyecto/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto'),
    path('proyecto/<int:pk>/delete/', views.ProyectoDeleteView.as_view(), name='proyecto_delete'),
    path('proyecto/<int:pk>/update/', views.ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyecto/<int:pk>/cliente/', views.ClienteDetailView.as_view(), name='cliente'),
    # TAREAS
    path('nueva_tareaJS/', views.TareaCreateView.as_view(), name='tarea_form'),
    path('tareas_listJS/', views.TareasListView.as_view(), name='tareas_list'),
    path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),
    path('tarea/<int:pk>/delete/', views.TareaDeleteView.as_view(), name='tarea_delete'),
    path('tarea/<int:pk>/update/', views.TareaUpdateView.as_view(), name='tarea_update'),
    # EMPLEADOS
    path('nuevo_empleado/', views.EmpleadoCreateView.as_view(), name='empleado_form'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('empleado/<int:pk>/delete/', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),
    path('empleado/<int:pk>/update/', views.EmpleadoUpdateView.as_view(), name='empleado_update'),
]
