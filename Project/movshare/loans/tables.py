from django_tables2 import tables, TemplateColumn
from .models import MediaRequest

class RequestTable(tables.Table):
    class Meta:
        model = MediaRequest
        attrs = {'class': 'table table-sm'}
        fields = ['name', 'media_type', 'description', 'delete']
        template_name = 'django_tables2/bootstrap.html'
    approve = TemplateColumn(temlpate_name = 'pages/tables/approvebtn.html')
    #add reject button in future


