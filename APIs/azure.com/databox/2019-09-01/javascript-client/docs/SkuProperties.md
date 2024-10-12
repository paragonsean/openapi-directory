# DataBoxManagementClient.SkuProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersions** | **[String]** | Api versions that support this Sku. | [optional] [readonly] 
**capacity** | [**SkuCapacity**](SkuCapacity.md) |  | [optional] 
**costs** | [**[SkuCost]**](SkuCost.md) | Cost of the Sku. | [optional] [readonly] 
**destinationToServiceLocationMap** | [**[DestinationToServiceLocationMap]**](DestinationToServiceLocationMap.md) | The map of destination location to service location. | [optional] [readonly] 
**disabledReason** | **String** | Reason why the Sku is disabled. | [optional] [readonly] 
**disabledReasonMessage** | **String** | Message for why the Sku is disabled. | [optional] [readonly] 
**requiredFeature** | **String** | Required feature to access the sku. | [optional] [readonly] 



## Enum: DisabledReasonEnum


* `None` (value: `"None"`)

* `Country` (value: `"Country"`)

* `Region` (value: `"Region"`)

* `Feature` (value: `"Feature"`)

* `OfferType` (value: `"OfferType"`)

* `NoSubscriptionInfo` (value: `"NoSubscriptionInfo"`)




