

# InappproductsUpdateRequest

Request to update an in-app product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowMissing** | **Boolean** | If set to true, and the in-app product with the given package_name and sku doesn&#39;t exist, the in-app product will be created. |  [optional] |
|**autoConvertMissingPrices** | **Boolean** | If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false. |  [optional] |
|**inappproduct** | [**InAppProduct**](InAppProduct.md) |  |  [optional] |
|**latencyTolerance** | [**LatencyToleranceEnum**](#LatencyToleranceEnum) | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. |  [optional] |
|**packageName** | **String** | Package name of the app. |  [optional] |
|**sku** | **String** | Unique identifier for the in-app product. |  [optional] |



## Enum: LatencyToleranceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED&quot; |
| LATENCY_SENSITIVE | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE&quot; |
| LATENCY_TOLERANT | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT&quot; |



