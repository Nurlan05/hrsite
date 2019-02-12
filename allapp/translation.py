from modeltranslation.translator import translator, TranslationOptions
from allapps.models import TourType
from allapps.models import Tours


class TourTypeTranslationOptions(TranslationOptions):
    fields = ('type_title', 'type_about')


translator.register(TourType, TourTypeTranslationOptions)

class ToursTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(Tours, ToursTranslationOptions)


