from django.db import models
from accounts.models import Person
from companies.models import Company
from documents.models import DocumentVersion
from projects.models import Project


class BCCompany(Company):
    bc_id = models.IntegerField()


class BCDocumentVersion(DocumentVersion):
    def __init__(self, *args, **kwargs):
        super(BCDocumentVersion, self).__init__(*args, **kwargs)
        self.file.field.null = True
        for field in self._meta.local_fields:
            if field.name == 'created':
                field.auto_add_now = False
            elif field.name == 'changed':
                field.auto_now_add = False

    bc_latest = models.BooleanField()
    bc_size = models.IntegerField()
    bc_collection = models.IntegerField()
    bc_id = models.IntegerField()
    bc_category = models.IntegerField(null=True, blank=True)
    bc_url = models.URLField(max_length=400)
    bc_project = models.ForeignKey('BCProject')


class BCPerson(Person):
    bc_id = models.IntegerField(null=True, blank=True)


class BCProject(Project):
    bc_id = models.IntegerField()
