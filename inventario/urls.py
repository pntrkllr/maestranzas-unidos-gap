from django.urls import path
from . import views
from .views import exportar_excel

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_inventario, name='registro'),
    path('registro-usuario/', views.registro_usuario, name='registro_usuario'),
    path('olvidar-contra/', views.olvidar_contra, name='olvidar_contra'),

    path('lista_productos/', views.lista_productos_view, name='lista_productos'),

    path('productos/registrar/', views.registro_producto, name='registro_producto'),
    path('productos/crud/', views.producto_crud, name='producto_crud'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),

    path('usuarios/', views.usuarios_crud, name='usuarios_crud'),

    path('carrito/', views.ver_carrito, name='ver_carrito'),

    path('productos/historial/<int:producto_id>/', views.historial_precios_producto, name='historial_precios'),

    path('movimientos/', views.listar_movimientos, name='listar_movimientos'),
    path('movimientos/registrar/', views.registrar_movimiento, name='registrar_movimiento'),
    path('productos/movimiento/<int:producto_id>/', views.registrar_movimiento_directo, name='registrar_movimiento_directo'),

    path('productos/eliminar-historial/<int:historial_id>/', views.eliminar_historial_precio, name='eliminar_historial_precio'),
    path('productos/eliminar-movimiento/<int:movimiento_id>/', views.eliminar_movimiento, name='eliminar_movimiento'),

    path('producto/<int:producto_id>/cambiar_bodega/', views.cambiar_bodega, name='cambiar_bodega'),

    path('panel_control/', views.panel_control_view, name='panel_control'),
    path('exportar-excel/', exportar_excel, name='exportar_excel'),

    path('logout/', views.logout_view, name='logout'),

]
