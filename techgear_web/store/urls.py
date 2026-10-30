
from django.urls import path
from . import views

urlpatterns = [
    # =========================
    # CATÁLOGO
    # =========================
    path("", views.catalogo, name="catalogo"),

    # =========================
    # AUTENTICACIÓN
    # =========================
    path("login/", views.login_view, name="login"),
    path("registro/", views.registro_view, name="registro"),
    path("logout/", views.logout_view, name="logout"),

    # =========================
    # PEDIDOS
    # =========================
    path("pedidos/", views.pedidos, name="pedidos"),
    path("pedidos/pagar/", views.pagar_pedidos, name="pagar_pedidos"),

    path(
        "pedidos/<str:pedido_id>/enviar/",
        views.marcar_pedido_enviado,
        name="marcar_pedido_enviado"
    ),

    path(
        "pedidos/<str:pedido_id>/recibir/",
        views.marcar_pedido_recibido,
        name="marcar_pedido_recibido"
    ),

    path(
        "pedir/<str:producto_id>/",
        views.pedir,
        name="pedir"
    ),

    # =========================
    # ADMINISTRACIÓN
    # =========================
    path(
        "panel/",
        views.panel_admin,
        name="panel_admin"
    ),

    # Editar producto
    path(
        "panel/editar/<str:producto_id>/",
        views.editar_producto,
        name="editar_producto"
    ),

    # Eliminar producto
    path(
        "panel/eliminar/<str:producto_id>/",
        views.eliminar_producto,
        name="eliminar_producto"
    ),
]
