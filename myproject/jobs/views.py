from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JobListing
from .serializers import JobListingSerializer

@api_view(['GET'])
def home(request):
    return HttpResponse("Welcome to the Job Listings API")

@api_view(['GET', 'POST'])
def job_listing_list(request):
    if request.method == 'GET':
        job_listings = JobListing.objects.all()
        serializer = JobListingSerializer(job_listings, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = JobListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def job_listing_detail(request, pk):
    try:
        job_listing = JobListing.objects.get(pk=pk)
    except JobListing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = JobListingSerializer(job_listing)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = JobListingSerializer(job_listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        job_listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
