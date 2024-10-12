# CloudBillingApi.PricingInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationInfo** | [**AggregationInfo**](AggregationInfo.md) |  | [optional] 
**currencyConversionRate** | **Number** | Conversion rate used for currency conversion, from USD to the currency specified in the request. This includes any surcharge collected for billing in non USD currency. If a currency is not specified in the request this defaults to 1.0. Example: USD * currency_conversion_rate &#x3D; JPY | [optional] 
**effectiveTime** | **String** | The timestamp from which this pricing was effective within the requested time range. This is guaranteed to be greater than or equal to the start_time field in the request and less than the end_time field in the request. If a time range was not specified in the request this field will be equivalent to a time within the last 12 hours, indicating the latest pricing info. | [optional] 
**pricingExpression** | [**PricingExpression**](PricingExpression.md) |  | [optional] 
**summary** | **String** | An optional human readable summary of the pricing information, has a maximum length of 256 characters. | [optional] 


