from django_elasticsearch_dsl import DocType, StringField, IntegerField

from mainapp.models.paper import Paper
from .utils import autocomplete_analyzer, mainIndex


@mainIndex.doc_type
class PaperDocument(DocType):
    autocomplete = StringField(attr="get_autocomplete", analyzer=autocomplete_analyzer)
    main_file = IntegerField(attr="main_file_id")
    person_ids = IntegerField(attr="person_ids")
    organization_ids = IntegerField(attr="organization_ids")

    class Meta:
        model = Paper

        fields = [
            'id',
            'name',
            'short_name',
            'description',
            'legal_date',
            'created',
            'modified',
            'sort_date',
        ]
