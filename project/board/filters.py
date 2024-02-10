# from django_filters import FilterSet
# from .models import *
#
# # Создаем свой набор фильтров для модели UserResponse.
# # FilterSet, который мы наследуем,
# # должен чем-то напомнить знакомые вам Django дженерики.
# class ResponseFilter(FilterSet):
#    class Meta:
#        # В Meta классе мы должны указать Django модель,
#        # в которой будем фильтровать записи.
#        model = Article
#        # В fields мы описываем по каким полям модели
#        # будет производиться фильтрация.
#        fields = {
#            # поиск по объяалениям
#            'article': ['icontains']
#            }