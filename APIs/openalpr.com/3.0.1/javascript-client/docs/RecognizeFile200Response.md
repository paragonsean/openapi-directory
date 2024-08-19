# OpenAlprCarCheckApi.RecognizeFile200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditCost** | **Number** | The number of API credits that were used to process this image | [optional] 
**creditsMonthlyTotal** | **Number** | The maximum number of API credits available this month according to your plan | [optional] 
**creditsMonthlyUsed** | **Number** | The number of API credits used this month | [optional] 
**dataType** | **String** | Specifies the type of data in this response | [optional] 
**epochTime** | **Number** | Epoch time that the image was processed in milliseconds | [optional] 
**imgHeight** | **Number** | Height of the input image in pixels | [optional] 
**imgWidth** | **Number** | Width of the uploaded image in pixels | [optional] 
**processingTime** | [**RecognizeFile200ResponseProcessingTime**](RecognizeFile200ResponseProcessingTime.md) |  | [optional] 
**regionsOfInterest** | [**[RegionOfInterest]**](RegionOfInterest.md) | Describes the areas analyzed in the input image | [optional] 
**results** | [**[PlateDetails]**](PlateDetails.md) |  | [optional] 
**vehicles** | [**[Vehicles]**](Vehicles.md) | Describes all vehicles found in the input image | [optional] 
**version** | **Number** | API format version | [optional] 



## Enum: DataTypeEnum


* `alpr_results` (value: `"alpr_results"`)

* `alpr_group` (value: `"alpr_group"`)

* `heartbeat` (value: `"heartbeat"`)




