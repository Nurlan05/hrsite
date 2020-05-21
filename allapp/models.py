from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from allapp.helper import slugify
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class AboutUs(models.Model):
	a_title=models.CharField(max_length=1500,verbose_name="Title")
	a_content=RichTextField(verbose_name="Content")
	def __str__(self):
		return ('%s') %(self.a_title)
	class Meta:
		verbose_name="About us"
		verbose_name_plural="About us"
	def save(self, *args, **kwargs):
	  	self.slug = slugify(self.a_title)
	  	super(AboutUs, self).save(*args, **kwargs)

class ContactUs(models.Model):
	email=models.EmailField(verbose_name="Email")
	telphone=models.CharField(max_length=1500,verbose_name="Telphone")
	location=models.CharField(max_length=1500,verbose_name="Location")
	def __str__(self):
		return ('%s') %(self.email)
	class Meta:
		verbose_name="Contact us"
		verbose_name_plural="Contact us"
	def save(self, *args, **kwargs):
	  	self.slug = slugify(self.email)
	  	super(ContactUs, self).save(*args, **kwargs)




class Location(models.Model):
	city_name=models.CharField(max_length=1500,verbose_name="City Name")
	slug=models.SlugField(editable=False,unique=True,verbose_name="Slug")
	def __str__(self):
		return ('%s') %(self.city_name)
	class Meta:
		verbose_name="City or Country"
		verbose_name_plural="Cities or Countries"
	def save(self, *args, **kwargs):
	  	self.slug = slugify(self.city_name)
	  	super(Location, self).save(*args, **kwargs)


class JobType(models.Model):
	job_name=models.CharField(max_length=1500,verbose_name="Job Type name")
	slug=models.SlugField(editable=False,unique=True,verbose_name="Slug")
	def __str__(self):
		return ('%s') %(self.job_name)
	class Meta:
		verbose_name="JobType"
		verbose_name_plural="JobTypes"
	def save(self, *args, **kwargs):
	  	self.slug = slugify(self.job_name)
	  	super(JobType, self).save(*args, **kwargs)



class Sector(models.Model):
	sector_name=models.CharField(max_length=1500,verbose_name="Sector name")
	slug=models.SlugField(editable=False,unique=True,verbose_name="Slug")
	def __str__(self):
		return ('%s') %(self.sector_name)
	class Meta:
		verbose_name="Sector"
		verbose_name_plural="Sectors"
	def save(self, *args, **kwargs):
	  	self.slug = slugify(self.sector_name)
	  	super(Sector, self).save(*args, **kwargs)


class ContractType(models.Model):
	contract_name=models.CharField(max_length=1500,verbose_name="Contract Name")
	slug=models.SlugField(editable=False,unique=True,verbose_name="Slug")
	def __str__(self):
		return ('%s') %(self.contract_name)
	class Meta:
		verbose_name="Contract Type"
		verbose_name_plural="Contract Types"
	def save(self, *args, **kwargs):
	  	self.slug = slugify(self.contract_name)
	  	super(ContractType, self).save(*args, **kwargs)



class ExperienceLevel(models.Model):
	experience_name=models.CharField(max_length=1500,verbose_name="Experience Name")
	slug=models.SlugField(editable=False,unique=True,verbose_name="Slug")
	def __str__(self):
		return ('%s') %(self.experience_name)
	class Meta:
		verbose_name="Experience Level"
		verbose_name_plural="Experience Levels"
	def save(self, *args, **kwargs):
	  	self.slug = slugify(self.experience_name)
	  	super(ExperienceLevel, self).save(*args, **kwargs)


class Hours(models.Model):
	hours_name=models.CharField(max_length=1500,verbose_name="Experience Name")
	slug=models.SlugField(editable=False,unique=True,verbose_name="Slug")
	def __str__(self):
		return ('%s') %(self.hours_name)
	class Meta:
		verbose_name="Hours"
		verbose_name_plural="Hours"
	def save(self, *args, **kwargs):
	  	self.slug = slugify(self.hours_name)
	  	super(Hours, self).save(*args, **kwargs)





class Job(models.Model):
	job_location=models.ManyToManyField(Location,related_name='location',verbose_name="Job location",)
	job_sector=models.ForeignKey(Sector,related_name='sector',verbose_name="Job sector",null=True,on_delete=models.CASCADE)
	job_type=models.ForeignKey(JobType,related_name='jobtype',verbose_name="Job Type",null=True,on_delete=models.CASCADE)
	job_contract_type=models.ForeignKey(ContractType,related_name='contracttype',verbose_name="Contract Type",null=True,on_delete=models.CASCADE)
	job_experience_level=models.ForeignKey(ExperienceLevel,related_name='experiencelevel',verbose_name="Experience Level",null=True,on_delete=models.CASCADE)
	job_hours=models.ForeignKey(Hours,related_name='hours',verbose_name="Hours",null=True,on_delete=models.CASCADE)

	title=models.CharField(max_length=1500,verbose_name="Job name",)
	salary=models.CharField(max_length=1500,verbose_name="Salary",null=True,blank=True)
	expiry_date=models.DateTimeField(verbose_name="Expiry Date",null=True,blank=True)
	email=models.CharField(max_length=1500,verbose_name="Email",null=True,blank=True)
	content=RichTextField(verbose_name="About job")
	draft=models.BooleanField(default=True,verbose_name="Public?",)
	created_at = models.DateTimeField(auto_now_add=True,null=True)
	slug=models.SlugField(editable=False,verbose_name="Slug")
	def __str__(self):
		return ('%s') %(self.title)
	def get_absolute_url(self):
		return reverse('allapp:job_detail',kwargs={'slug':self.slug})
	class Meta:
		verbose_name="Vacancy"
		verbose_name_plural="Vacancies"
		ordering=['-id']
	def save(self, *args, **kwargs):
	  	super(Job, self).save(*args, **kwargs)
	  	self.slug = "{}-{}".format(slugify(self.title), self.id)
	  	super(Job, self).save(*args, **kwargs)
    


class CvSend(models.Model):
	name=models.CharField(max_length=1500,verbose_name="Ad")
	surname=models.CharField(max_length=1500,verbose_name="Soyad")
	apply_for=models.CharField(max_length=1500,verbose_name="Job slug",editable=False,null=True,blank=True)
	apply_name=models.CharField(max_length=1500,verbose_name="Job name",editable=False,null=True,blank=True)

	email=models.EmailField(max_length=1500,verbose_name="Email")
	created_date=models.DateTimeField(auto_now_add=True,null=True)
	cv=models.FileField(verbose_name='Cv')
	cover_letter=models.FileField(verbose_name="Məktub")
	def __str__(self):
		return ('%s') %(self.name + " " + self.surname)
	class Meta:
		verbose_name="CV"
		verbose_name_plural="ALL CV"
		ordering=['-id']
