

# RecognizeFile200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creditCost** | **Integer** | The number of API credits that were used to process this image |  [optional] |
|**creditsMonthlyTotal** | **Integer** | The maximum number of API credits available this month according to your plan |  [optional] |
|**creditsMonthlyUsed** | **Integer** | The number of API credits used this month |  [optional] |
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | Specifies the type of data in this response |  [optional] |
|**epochTime** | **BigDecimal** | Epoch time that the image was processed in milliseconds |  [optional] |
|**imgHeight** | **Integer** | Height of the input image in pixels |  [optional] |
|**imgWidth** | **Integer** | Width of the uploaded image in pixels |  [optional] |
|**processingTime** | [**RecognizeFile200ResponseProcessingTime**](RecognizeFile200ResponseProcessingTime.md) |  |  [optional] |
|**regionsOfInterest** | [**List&lt;RegionOfInterest&gt;**](RegionOfInterest.md) | Describes the areas analyzed in the input image |  [optional] |
|**results** | [**List&lt;PlateDetails&gt;**](PlateDetails.md) |  |  [optional] |
|**vehicles** | [**List&lt;Vehicles&gt;**](Vehicles.md) | Describes all vehicles found in the input image |  [optional] |
|**version** | **Integer** | API format version |  [optional] |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| ALPR_RESULTS | &quot;alpr_results&quot; |
| ALPR_GROUP | &quot;alpr_group&quot; |
| HEARTBEAT | &quot;heartbeat&quot; |



