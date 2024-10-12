# AwsElementalMediaPackage.CreateHarvestJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | The end of the time-window which will be harvested  | 
**id** | **String** | The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted  | 
**originEndpointId** | **String** | The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.  | 
**s3Destination** | [**CreateHarvestJobRequestS3Destination**](CreateHarvestJobRequestS3Destination.md) |  | 
**startTime** | **String** | The start of the time-window which will be harvested  | 


