from django import template
# models.pyのある階層は2つ上なので、`..`とする
from ..models import Category

register = template.Library()

@register.filter
def all_attr(bound_form):
    # すべてのフィールドではattrが共通と思われるので、
    # 最初のでだけ確認すればいいはず
    for f in bound_form:
        return dir(f)

@register.filter
def data_verbose(bound_field):
    if bound_field.auto_id == 'formtools_categories':
        result = [Category.objects.get(pk=d).name for d in bound_field.data]
        return ','.join(result)

    return bound_field.data