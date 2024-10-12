# TravelPartnerApi.PriceCoverageView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculationDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**matchedPropertyCount** | **Number** | The total number of properties that have prices for the given itineraries. | [optional] 
**priceCoverageBinaryPercent** | **Number** | The ratio between the number of hotels which have at least one price for the calculation period and &#x60;matched_property_count&#x60;. | [optional] 
**priceCoverageBuckets** | [**[PriceCoverageBucket]**](PriceCoverageBucket.md) | Price coverage stats for combinations of advance booking window and length of stay ranges. | [optional] 
**priceCoveragePercent** | **Number** | The overall price coverage for an account. This value is the ratio between the number of hotel prices for the calculation booking window and length of stay range divided by the number of all possible prices, which is &#x60;matched_property_count&#x60; times 330 (for advance book window) times 30 (for length of stay). | [optional] 


