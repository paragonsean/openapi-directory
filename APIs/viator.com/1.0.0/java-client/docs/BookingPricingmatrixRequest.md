

# BookingPricingmatrixRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookingDate** | **String** | **date** for which to retrieve pricing data  (must be in the future) (**note**: this is an optional parameter for normal products; if the date is *not* provided then the nearest available date is determined) |  [optional] |
|**currencyCode** | **String** | **currency code** of the currency in which to display pricing information |  [optional] |
|**productCode** | **String** | **unique alphanumeric identifier** of the product for which to retrieve the pricing matrix |  [optional] |
|**tourGradeCode** | **String** | **alphanumeric identifier** of the product tour grade for which to retrieve the pricing matrix |  [optional] |



