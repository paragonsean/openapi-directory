

# OrderPickupDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**OrderAddress**](OrderAddress.md) |  |  [optional] |
|**collectors** | [**List&lt;OrderPickupDetailsCollector&gt;**](OrderPickupDetailsCollector.md) | Collectors authorized to pick up shipment from the pickup location. |  [optional] |
|**locationId** | **String** | ID of the pickup location. |  [optional] |
|**pickupType** | **String** | The pickup type of this order. Acceptable values are: - \&quot;&#x60;merchantStore&#x60;\&quot; - \&quot;&#x60;merchantStoreCurbside&#x60;\&quot; - \&quot;&#x60;merchantStoreLocker&#x60;\&quot; - \&quot;&#x60;thirdPartyPickupPoint&#x60;\&quot; - \&quot;&#x60;thirdPartyLocker&#x60;\&quot;  |  [optional] |



