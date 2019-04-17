from django_tables2 import tables, TemplateColumn
from .models import MediaRequest

class RequestTable(tables.Table):
    class Meta:
        model = MediaRequest
        attrs = {'class': 'table table-sm'}
        fields = ['requester', 'media.name', 'media.media_type', 'media.description']
        template_name = 'django_tables2/bootstrap.html'
    approve = TemplateColumn(template_name = 'pages/tables/approvebtn.html')

class RequestTable(tables.Table):
    class Meta:
        model = MediaRequest
        attrs = {'class': 'table table-sm'}
        fields = ['media.owner', 'media.name', 'media.media_type', 'media.description']
        template_name = 'django_tables2/bootstrap.html'
    approve = TemplateColumn(template_name = 'pages/tables/returnbtn.html')


