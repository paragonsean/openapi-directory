

# WarehouseBasedDeliveryTime


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrier** | **String** | Required. Carrier, such as &#x60;\&quot;UPS\&quot;&#x60; or &#x60;\&quot;Fedex\&quot;&#x60;. The list of supported carriers can be retrieved through the &#x60;listSupportedCarriers&#x60; method. |  [optional] |
|**carrierService** | **String** | Required. Carrier service, such as &#x60;\&quot;ground\&quot;&#x60; or &#x60;\&quot;2 days\&quot;&#x60;. The list of supported services for a carrier can be retrieved through the &#x60;listSupportedCarriers&#x60; method. The name of the service must be in the eddSupportedServices list. |  [optional] |
|**originAdministrativeArea** | **String** | Shipping origin&#39;s state. |  [optional] |
|**originCity** | **String** | Shipping origin&#39;s city. |  [optional] |
|**originCountry** | **String** | Shipping origin&#39;s country represented as a [CLDR territory code](https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml). |  [optional] |
|**originPostalCode** | **String** | Shipping origin. |  [optional] |
|**originStreetAddress** | **String** | Shipping origin&#39;s street address. |  [optional] |
|**warehouseName** | **String** | The name of the warehouse. Warehouse name need to be matched with name. If warehouseName is set, the below fields will be ignored. The warehouse info will be read from warehouse. |  [optional] |



