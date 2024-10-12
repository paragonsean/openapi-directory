# GooglePlayAndroidDeveloperApi.UpdateSubscriptionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMissing** | **Boolean** | Optional. If set to true, and the subscription with the given package_name and product_id doesn&#39;t exist, the subscription will be created. If a new subscription is created, update_mask is ignored. | [optional] 
**latencyTolerance** | **String** | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. | [optional] 
**regionsVersion** | [**RegionsVersion**](RegionsVersion.md) |  | [optional] 
**subscription** | [**Subscription**](Subscription.md) |  | [optional] 
**updateMask** | **String** | Required. The list of fields to be updated. | [optional] 



## Enum: LatencyToleranceEnum


* `UNSPECIFIED` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"`)

* `LATENCY_SENSITIVE` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE"`)

* `LATENCY_TOLERANT` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT"`)




