import csv

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from csv_processing_api import serializers


class CsvProcessingView(APIView):

    serializers_class = serializers.CsvSerializer

    def get(self, request, format=None):
        an_apiview = [
            'attach csv file'
        ]

        return Response({'an_apiview': an_apiview})


    def post(self, request):
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            csvfile = serializer.validated_data.get('csvfile')

            with open(csvfile, encoding='utf8') as data:
                reader = csv.DictReader(data, delimiter=',')
                next(reader, None)

                total_cost = 0
                counter = 0

                for line in reader:
                    if line['country'] == 'USA':
                        budget = line['budget']
                        budget = budget[2:]
                    if budget.isdigit():
                        number_budget = int(budget)

                    total_cost += number_budget
                    counter += 1
                
            average_cost = total_cost / counter
        
            return Response({'total_cost': total_cost, 'avarege_cost': avarege_cost})

