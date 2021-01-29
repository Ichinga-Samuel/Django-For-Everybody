from django.contrib import admin
from unesco.models import Site, Category, Iso, State, Region


[admin.site.register(i) for i in (Site, Category, Iso, State, Region)]
