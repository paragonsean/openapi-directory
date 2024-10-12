# GooglePlayAndroidDeveloperApi.UpdateSubscriptionOfferRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMissing** | **Boolean** | Optional. If set to true, and the subscription offer with the given package_name, product_id, base_plan_id and offer_id doesn&#39;t exist, an offer will be created. If a new offer is created, update_mask is ignored. | [optional] 
**latencyTolerance** | **String** | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. | [optional] 
**regionsVersion** | [**RegionsVersion**](RegionsVersion.md) |  | [optional] 
**subscriptionOffer** | [**SubscriptionOffer**](SubscriptionOffer.md) |  | [optional] 
**updateMask** | **String** | Required. The list of fields to be updated. | [optional] 



## Enum: LatencyToleranceEnum


* `UNSPECIFIED` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"`)

* `LATENCY_SENSITIVE` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE"`)

* `LATENCY_TOLERANT` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT"`)




