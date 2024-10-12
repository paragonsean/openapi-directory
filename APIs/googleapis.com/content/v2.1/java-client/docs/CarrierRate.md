

# CarrierRate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierName** | **String** | Carrier service, such as &#x60;\&quot;UPS\&quot;&#x60; or &#x60;\&quot;Fedex\&quot;&#x60;. The list of supported carriers can be retrieved through the &#x60;getSupportedCarriers&#x60; method. Required. |  [optional] |
|**carrierService** | **String** | Carrier service, such as &#x60;\&quot;ground\&quot;&#x60; or &#x60;\&quot;2 days\&quot;&#x60;. The list of supported services for a carrier can be retrieved through the &#x60;getSupportedCarriers&#x60; method. Required. |  [optional] |
|**flatAdjustment** | [**Price**](Price.md) |  |  [optional] |
|**name** | **String** | Name of the carrier rate. Must be unique per rate group. Required. |  [optional] |
|**originPostalCode** | **String** | Shipping origin for this carrier rate. Required. |  [optional] |
|**percentageAdjustment** | **String** | Multiplicative shipping rate modifier as a number in decimal notation. Can be negative. For example &#x60;\&quot;5.4\&quot;&#x60; increases the rate by 5.4%, &#x60;\&quot;-3\&quot;&#x60; decreases the rate by 3%. Optional. |  [optional] |



