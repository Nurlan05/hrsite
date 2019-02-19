from modeltranslation.translator import translator, TranslationOptions
from allapp.models import AboutUs,ContactUs,Job,Location,Sector,JobType,ExperienceLevel,ContractType,Hours


class JobTranslationOptions(TranslationOptions):
	fields=('title','content')

translator.register(Job, JobTranslationOptions)


class LocationTranslationOptions(TranslationOptions):
	fields=('city_name',)

translator.register(Location, LocationTranslationOptions)



class SectorTranslationOptions(TranslationOptions):
	fields=('sector_name',)

translator.register(Sector, SectorTranslationOptions)

class JobTypeTranslationOptions(TranslationOptions):
	fields=('job_name',)

translator.register(JobType, JobTypeTranslationOptions)



class ExperienceLevelTranslationOptions(TranslationOptions):
	fields=('experience_name',)

translator.register(ExperienceLevel, ExperienceLevelTranslationOptions)




class HoursTranslationOptions(TranslationOptions):
	fields=('hours_name',)

translator.register(Hours, HoursTranslationOptions)




class ContractTypeTranslationOptions(TranslationOptions):
	fields=('contract_name',)

translator.register(ContractType, ContractTypeTranslationOptions)

class AboutUsTranslationOptions(TranslationOptions):
	fields=('a_title','a_content')

translator.register(AboutUs, AboutUsTranslationOptions)