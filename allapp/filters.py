from allapp.models import Job
import django_filters
class JobFilter(django_filters.FilterSet):



    class Meta:
        model = Job
        fields = [
        'job_location',
        'job_sector',
        'job_type',
        'job_contract_type', 
        'job_experience_level',
        'job_hours',
        ]