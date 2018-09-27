from rest_framework import serializers
from .models import Company, Office
from django.db.models import Sum



class CompanySerializer(serializers.ModelSerializer):
    monthly_rent_sum = serializers.SerializerMethodField()

    def get_monthly_rent_sum(self, obj):
        return obj.offices.aggregate(
            Sum('monthly_rent')
        )['monthly_rent__sum']

    class Meta:
        model = Company
        fields = ('id', 'name', 'headquarter', 'monthly_rent_sum')



class OfficeSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company.name

    class Meta:
        model = Office
        fields = ('street', 'postal_code', 'city', 'company_name')
