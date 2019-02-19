from django.contrib import admin
from .models import AboutUs,ContactUs,CvSend,Job,Location,Sector,JobType,ExperienceLevel,ContractType,Hours


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
	exclude=('a_title','a_content')
	list_display = ('a_title',)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
	list_display = ('email','telphone','location')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	exclude=('city_name',)
	list_display = ('city_name','slug')

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
	exclude=('sector_name',)
	list_display = ('sector_name','slug')


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
	exclude=('job_name',)
	list_display = ('job_name','slug')

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
	exclude=('contract_name',)
	list_display = ('contract_name','slug')



@admin.register(ExperienceLevel)
class ExperienceLevelAdmin(admin.ModelAdmin):
	exclude=('experience_name',)
	list_display = ('experience_name','slug')


@admin.register(Hours)
class HoursAdmin(admin.ModelAdmin):
	exclude=('hours_name',)
	list_display = ('hours_name','slug')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
	exclude=('title','content')
	list_display = ('title','slug')
	search_fields = ('title', 'content')
@admin.register(CvSend)
class CvSendAdmin(admin.ModelAdmin):
	list_display = ('name','surname','apply_name','created_date')
	list_display_link=('name','surname')