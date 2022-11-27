from django import forms


class HistVentForm(forms.Form):

	MEDIO_DE_PAGO_CHOICES = (
	(1,"Efectivo"),
	(2,"Tarjeta"),
	(3,"Mercadopago"),
	)

	TIENDA_CHOICES = (
	(1,"Fisica"),
	(2,"Online"),
	)

	fecha_inicial =  forms.DateField(widget=forms.SelectDateWidget(years=['2020','2021','2022']))
	fecha_final =  forms.DateField(widget=forms.SelectDateWidget(years=['2020','2021','2022']))
	producto = forms.CharField(label="producto", required=True)
	medio_de_pago = forms.ChoiceField(label="medio_de_pago", choices=MEDIO_DE_PAGO_CHOICES)
	tienda_fisica_u_online = forms.ChoiceField(label="tienda", choices=TIENDA_CHOICES)
	


	#EJEMPLO DE FORMULARIO
	# class ContactoForm(forms,Form):
	# 	TORNEO_CHOICES = (
	# 	(1,"opcion 1"),
	# 	(2,"opcion 2"),
	# 	(3,"opcion 3"),
	# 	)
	# 	nombre = forms.CharField(label="Nombre de contacto", required=True)
	# 	apellido = forms.CharField(label="Apellido de contacto",required=True)
	# 	email = forms.EmailField(required=True)
	# 	sitio_favorito = forms.URLField(label="sitio favorito")
	# 	nacimiento =  forms.DateField(widget=forms.SelectDateWidget(years['2020','2021','2022']))
	# 	torneo_favorito = forms.ChoiceField(label="Torneo Favorito", choices=TORNEO_CHOICES)
