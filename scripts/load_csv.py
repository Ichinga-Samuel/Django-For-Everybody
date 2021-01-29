import csv

from unesco.models import Site, Category, Iso, State, Region


def load_db():
    [m.objects.all().delete() for m in [Site, Category, Iso, State, Region]]
    ch = open('unesco/whc-sites-2018-clean.csv')
    cr = csv.reader(ch)
    next(cr)
    for r in cr:
        m, c = Category.objects.get_or_create(name=r[7])
        i, c = Iso.objects.get_or_create(name=r[10])
        s, c = State.objects.get_or_create(name=r[8])
        re, c = Region.objects.get_or_create(name=r[9])
        d = dict(year=r[3], longitude=r[4], latitude=r[5], area_hectares=r[6])
        for k, j in d.items():
            try:
                if k == 'year':
                    d[k] = int(j)
                else:
                    d[k] = float(j)
            except ValueError:
                d[k] = None

        si, c = Site.objects.get_or_create(name=r[0], description=r[1], justification=r[2], year=d['year'],
                                           longitude=d['longitude'], latitude=d['latitude'],
                                           area_hectares=d['area_hectares'],
                                           category=m, state=s, region=re, iso=i)


load_db()
