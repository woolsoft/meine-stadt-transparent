from django.db import models
from djgeojson.fields import GeometryField

from .body import Body
from .default_fields import DefaultFields


class SearchPoi(DefaultFields):
    displayed_name = models.CharField(max_length=1000)
    bodies = models.ManyToManyField(Body, blank=True)
    osm_id = models.BigIntegerField(null=True, blank=True)
    osm_amenity = models.CharField(null=True, max_length=1000)
    geometry = GeometryField(null=True)
    exclude_from_search = models.BooleanField(default=False)
