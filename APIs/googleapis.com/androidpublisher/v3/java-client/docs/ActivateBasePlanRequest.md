

# ActivateBasePlanRequest

Request message for ActivateBasePlan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basePlanId** | **String** | Required. The unique base plan ID of the base plan to activate. |  [optional] |
|**latencyTolerance** | [**LatencyToleranceEnum**](#LatencyToleranceEnum) | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. |  [optional] |
|**packageName** | **String** | Required. The parent app (package name) of the base plan to activate. |  [optional] |
|**productId** | **String** | Required. The parent subscription (ID) of the base plan to activate. |  [optional] |



## Enum: LatencyToleranceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED&quot; |
| LATENCY_SENSITIVE | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE&quot; |
| LATENCY_TOLERANT | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT&quot; |



