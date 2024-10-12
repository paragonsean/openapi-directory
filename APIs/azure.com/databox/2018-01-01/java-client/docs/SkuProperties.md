

# SkuProperties

Properties of the sku.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersions** | **List&lt;String&gt;** | Api versions that support this Sku. |  [optional] [readonly] |
|**capacity** | [**SkuCapacity**](SkuCapacity.md) |  |  [optional] |
|**costs** | [**List&lt;SkuCost&gt;**](SkuCost.md) | Cost of the Sku. |  [optional] [readonly] |
|**destinationToServiceLocationMap** | [**List&lt;DestinationToServiceLocationMap&gt;**](DestinationToServiceLocationMap.md) | The map of destination location to service location. |  [optional] [readonly] |
|**disabledReason** | [**DisabledReasonEnum**](#DisabledReasonEnum) | Reason why the Sku is disabled. |  [optional] [readonly] |
|**disabledReasonMessage** | **String** | Message for why the Sku is disabled. |  [optional] [readonly] |
|**requiredFeature** | **String** | Required feature to access the sku. |  [optional] [readonly] |



## Enum: DisabledReasonEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| COUNTRY | &quot;Country&quot; |
| REGION | &quot;Region&quot; |
| FEATURE | &quot;Feature&quot; |
| OFFER_TYPE | &quot;OfferType&quot; |
| NO_SUBSCRIPTION_INFO | &quot;NoSubscriptionInfo&quot; |



