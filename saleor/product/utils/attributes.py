def get_product_attributes_data(product):
    """Returns attributes associated with the product,
    as dict of Attribute: AttributeValue values.
    """
    attributes = product.product_type.product_attributes.all()
    return get_xxx_attributes_data(product, attributes)


def get_variant_attributes_data(product):
    """Same as get_product_attributes_data but for variants

    Test with `./manage.sh shell < tests/test_product_utils.py`
    """
    attributes = product.product_type.variant_attributes.all()
    return get_xxx_attributes_data(product, attributes, for_variant=True)


def get_xxx_attributes_data(product, attributes, for_variant=False):
    attributes_map = {
        attribute.pk: attribute.translated for attribute in attributes}

    def get_single(values_map):
      return {
        attributes_map[attr_pk]: value_obj.translated
        for (attr_pk, value_obj) in values_map.items()}

    if not for_variant:
      values_map = get_attributes_display_map(product, attributes)
      return get_single(values_map)

    out = {}
    for v in product.variants.all():
      values_map = get_attributes_display_map(v, attributes)
      out[v] = get_single(values_map)

    return out


def get_name_from_attributes(variant, attributes):
    """Generates ProductVariant's name based on its attributes."""
    values = get_attributes_display_map(variant, attributes)
    return generate_name_from_values(values)


def get_attributes_display_map(obj, attributes):
    """Returns attributes associated with an object,
    as dict of Attribute: AttributeValue values.

    Args:
        attributes: Attribute Iterable
    """
    display_map = {}
    for attribute in attributes:
        value = obj.attributes.get(str(attribute.pk))
        if value:
            choices = {str(a.pk): a.translated for a in attribute.values.all()}
            display_map[attribute.pk] = choices[value]
    return display_map


def generate_name_from_values(attributes_dict):
    """Generates name from AttributeValues. Attributes dict is sorted,
    as attributes order should be kept within each save.

    Args:
        attributes_dict: dict of attribute_pk: AttributeValue values
    """
    return ' / '.join(
        str(attribute_value)
        for attribute_pk, attribute_value in sorted(
            attributes_dict.items(),
            key=lambda x: x[0]))
