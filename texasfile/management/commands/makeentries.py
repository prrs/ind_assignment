from django.core.management.base import BaseCommand, CommandError
from texasfile.models import Resource, Image
import csv

class Command(BaseCommand):
    #def add_arguments(self, parser):
    #    parser.add_argument('index_file', type=str)

    def handle(self, *args, **options):
        #f_name = options['index_file']
        print args
        f_name = args[0]
        with open(f_name, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            # handling non-breakable space character
            for row in reader:
                r = Resource()
                r.number = row[0].strip(' \t\xc2\xa0')
                r.volume = row[1].strip(' \t\xc2\xa0')
                r.page = int(row[2].strip(' \t\xc2\xa0'))
                r.save()
                for im in row[3:]:
                    print im
                    i = Image()
                    i.img = im.strip(' \t\xc2\xa0')
                    i.resource = r
                    i.save()
                
            

