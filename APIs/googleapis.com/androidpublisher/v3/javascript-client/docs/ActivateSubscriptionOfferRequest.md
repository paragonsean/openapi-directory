# GooglePlayAndroidDeveloperApi.ActivateSubscriptionOfferRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basePlanId** | **String** | Required. The parent base plan (ID) of the offer to activate. | [optional] 
**latencyTolerance** | **String** | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. | [optional] 
**offerId** | **String** | Required. The unique offer ID of the offer to activate. | [optional] 
**packageName** | **String** | Required. The parent app (package name) of the offer to activate. | [optional] 
**productId** | **String** | Required. The parent subscription (ID) of the offer to activate. | [optional] 



## Enum: LatencyToleranceEnum


* `UNSPECIFIED` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"`)

* `LATENCY_SENSITIVE` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE"`)

* `LATENCY_TOLERANT` (value: `"PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT"`)




