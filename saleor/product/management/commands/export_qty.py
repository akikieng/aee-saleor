from django.core.management.base import BaseCommand

def export_qty(fn_out):
  from saleor.product.models import ProductVariant, Attribute
  import pandas as pd
  qs=ProductVariant.objects.values('sku', 'name', 'product__name', 'quantity', 'quantity_allocated', 'cost_price', 'price_override')
  df=pd.DataFrame(list(qs))
  df.set_index('sku', inplace=True)

  if fn_out is None:
    print(df)
  else:
    df.to_csv(fn_out, index=True)

# ---------------------------
# variant attributes
# from saleor.product.utils.attributes import get_variant_attributes_data
# get_variant_attributes_data(ProductVariant.objects.first().product)

# ---------------------------

class Command(BaseCommand):
    help = """exports qty to csv (for reconciling with external sources)

    e.g.
    > pew in AEE_SALEOR ./manage.sh export_qty --fn_out="~/bitbucket.org/akikieng/inventory-gitdb/saleor.csv"
    """

    def add_arguments(self, parser):
      parser.add_argument('--fn_out', dest='fn_out', default=None, help='name of csv to which to save. Skip of stdout', type=str)


    def handle(self, *args, **options):
      export_qty(options['fn_out'])
