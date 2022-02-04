
from django import forms


class FormRegistrarEntrada(forms.Form):

    tituloEntrada = forms.CharField(required=True,
                                    min_length=20,
                                    max_length=120,
                                    widget=forms.TextInput(attrs={
                                        'class':'form-control border border-dark',
                                        'id':'tituloentrada',
                                        'name':'tituloentrada',
                                        'placeholder':'Ingrese el Titulo de la entrada'
                                    })
    )
    
    contenidoEntrada=forms.CharField(required=True,
                                     min_length=20,
                                     max_length=120,
                                     widget=forms.Textarea(attrs={
                                        'class':'form-control border border-dark',
                                        'id':'contenidoentrada',
                                        'name':'contenidoentrada',
                                        'cols':'30',
                                        'rows':'10',
                                        'placeholder':'Ingrese el contenido de la entrada',
                                        'style':'min-height:300px'
                                        
                                    })
    )

    # imagenDestacada= forms.ImageField(required=True)
    # categoriasEntrada = forms.ChoiceField()
   
