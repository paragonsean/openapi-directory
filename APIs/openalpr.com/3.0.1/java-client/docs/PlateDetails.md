

# PlateDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**candidates** | [**List&lt;PlateCandidate&gt;**](PlateCandidate.md) | All the top N candidates that could be the correct plate number |  [optional] |
|**confidence** | **BigDecimal** | Confidence percentage that the plate number is correct |  [optional] |
|**coordinates** | [**List&lt;Coordinate&gt;**](Coordinate.md) | The X/Y coordinates of the license plate in the image Four coordinates are provided that form a polygon starting from the top-left and moving clockwise ending in the bottom left  |  [optional] |
|**matchesTemplate** | **Integer** | Indicates whether the plate matched a regional text pattern |  [optional] |
|**plate** | **String** | Best plate number for this plate |  [optional] |
|**processingTimeMs** | **BigDecimal** | Number of milliseconds to process the license plate |  [optional] |
|**region** | **String** | Specified or detected region (e.g., tx for Texas) |  [optional] |
|**regionConfidence** | **BigDecimal** | Confidence percentage that the plate region is correct |  [optional] |
|**requestedTopn** | **Integer** | The max number of results requested |  [optional] |
|**vehicle** | [**VehicleDetails**](VehicleDetails.md) |  |  [optional] |
|**vehicleRegion** | [**RegionOfInterest**](RegionOfInterest.md) |  |  [optional] |



