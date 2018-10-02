from saleor.product.models import Product
from saleor.product.utils.attributes import get_product_attributes_data, get_variant_attributes_data
product=Product.objects.filter(name__contains='Large').first()
print('prod attr')
print(get_product_attributes_data(product))

print('variant attr')
print(get_variant_attributes_data(product))
