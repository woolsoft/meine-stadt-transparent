from django.db import models
from django.urls import reverse
from django.utils.translation import pgettext

from .body import Body
from .default_fields import DefaultFields, ShortableNameFields
from .legislative_term import LegislativeTerm
from .location import Location
from .organization_type import OrganizationType

ORGANIZATION_TYPE_NAMES = {
    "parliamentary group": pgettext('Document Type Name', 'Parliamentary Group'),
    "committee": pgettext('Document Type Name', 'Committee'),
    "department": pgettext('Document Type Name', 'Department'),
    "organization": pgettext('Document Type Name', 'Organization'),
}

ORGANIZATION_TYPE_NAMES_PLURAL = {
    "parliamentary group": pgettext('Document Type Name', 'Parliamentary Groups'),
    "committee": pgettext('Document Type Name', 'Committees'),
    "department": pgettext('Document Type Name', 'Departments'),
    "organization": pgettext('Document Type Name', 'Organizations'),
}


class Organization(DefaultFields, ShortableNameFields):
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    body = models.ForeignKey(Body, on_delete=models.CASCADE)
    legislative_terms = models.ManyToManyField(LegislativeTerm, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)
    # html color without the hash
    color = models.CharField(max_length=6, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name

    # A workaround to prevent empty values in the autocomplete-field in elasticsearch, which throws an error
    def name_autocomplete(self):
        return self.name if len(self.name) > 0 else ' '

    def get_default_link(self):
        return reverse('organization', args=[self.id])

    def sort_date(self):
        return self.start
