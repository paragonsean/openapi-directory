

# BookingPricingmatrix200ResponseAllOfDataInnerAgeBandPricesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandId** | **Integer** | **unique numeric identifier** for the age band - See: [Working with age bands](#section/Appendices/Working-with-age-bands)  |  [optional] |
|**maximumCountRequired** | **Integer** | **maximum number of travelers** that this pricing schedule can be applied to - use this field to specify the largest group size you are interested in making a booking for  |  [optional] |
|**minimumCountRequired** | **Integer** | **minimum number of travelers** that this pricing schedule can be applied to - use this field to specify the smallest group size you are interested in making a booking for  |  [optional] |
|**prices** | [**List&lt;BookingPricingmatrix200ResponseAllOfDataInnerAgeBandPricesInnerPricesInner&gt;**](BookingPricingmatrix200ResponseAllOfDataInnerAgeBandPricesInnerPricesInner.md) | **array** of prices available for *this* age band (based on the min and max count required) |  [optional] |
|**sortOrder** | **Integer** | **sort order** for *this* age band |  [optional] |



