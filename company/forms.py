from django import forms

from company.models import Request, ProductValue, RequestValue

class RequestForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product')
        super(RequestForm, self).__init__(*args, **kwargs)

        for value in self.product.values.all():
            self.fields['value_%s' % value.pk] = forms.CharField(label=value.value.title)

        #for i, question in enumerate(extra):
        #    self.fields['custom_%s' % i] = forms.CharField(label=question)

    def save(self):
        request = Request.objects.create(
            product=self.product,
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email']
        )

        for name, value in self.cleaned_data.items():
            if name.startswith('value_'):
                print(name[6:], value)
                source = ProductValue.objects.get(pk=int(name[6:]))
                RequestValue.objects.create(request=request,source=source,value=str(value))
