from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CompanySerializer, OfficeSerializer
from .models import Company, Office


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    @action(detail=True)
    def headquarter(self, request, pk):
        data = {}
        headquarter = self.get_object().headquarter
        if headquarter:
            data = OfficeSerializer(headquarter).data
        return Response(data)

    @action(detail=True)
    def offices(self, request, pk):
        offices = self.get_object().offices.all()
        return Response(OfficeSerializer(offices, many=True).data)

    def update(self, request, pk=None):
        """
        Allow to change only the headquarter
        """
        headquarter = request.data.get('headquarter')

        try:
            Office.objects.get(id=headquarter)
        except Office.DoesNotExist:
            return Response(
                'Office {} does not exist'.format(headquarter),
                status=400
            )

        instance = self.get_object()
        serializer = self.serializer_class(
            instance, data={'headquarter': headquarter}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
