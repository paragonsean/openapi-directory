

# DeactivateSubscriptionOfferRequest

Request message for DeactivateSubscriptionOffer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basePlanId** | **String** | Required. The parent base plan (ID) of the offer to deactivate. |  [optional] |
|**latencyTolerance** | [**LatencyToleranceEnum**](#LatencyToleranceEnum) | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. |  [optional] |
|**offerId** | **String** | Required. The unique offer ID of the offer to deactivate. |  [optional] |
|**packageName** | **String** | Required. The parent app (package name) of the offer to deactivate. |  [optional] |
|**productId** | **String** | Required. The parent subscription (ID) of the offer to deactivate. |  [optional] |



## Enum: LatencyToleranceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED&quot; |
| LATENCY_SENSITIVE | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE&quot; |
| LATENCY_TOLERANT | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT&quot; |



