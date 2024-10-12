

# ShippingZone


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**countries** | **List&lt;String&gt;** | Countries covered by the shipping zone. A country can only belong to one shipping zone (no overlapping). This property can be empty or null to create a default shipping zone for countries that were not specified in other zones.  |  [optional] |
|**createdTime** | **OffsetDateTime** | The shipping zone created time. |  [optional] [readonly] |
|**id** | **String** | The shipping zone identifier string. |  [optional] [readonly] |
|**isDefault** | **Object** | Is this Shipping Zone default. |  [optional] [readonly] |
|**name** | **String** | The shipping zone name. |  |
|**rates** | [**List&lt;PriceBasedShippingRate&gt;**](PriceBasedShippingRate.md) | Price-based shipping rate instructions. |  [optional] |
|**updatedTime** | **OffsetDateTime** | The shipping zone updated time. |  [optional] [readonly] |



