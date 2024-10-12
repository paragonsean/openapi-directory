

# MigrateBasePlanPricesRequest

Request message for MigrateBasePlanPrices.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basePlanId** | **String** | Required. The unique base plan ID of the base plan to update prices on. |  [optional] |
|**latencyTolerance** | [**LatencyToleranceEnum**](#LatencyToleranceEnum) | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. |  [optional] |
|**packageName** | **String** | Required. Package name of the parent app. Must be equal to the package_name field on the Subscription resource. |  [optional] |
|**productId** | **String** | Required. The ID of the subscription to update. Must be equal to the product_id field on the Subscription resource. |  [optional] |
|**regionalPriceMigrations** | [**List&lt;RegionalPriceMigrationConfig&gt;**](RegionalPriceMigrationConfig.md) | Required. The regional prices to update. |  [optional] |
|**regionsVersion** | [**RegionsVersion**](RegionsVersion.md) |  |  [optional] |



## Enum: LatencyToleranceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED&quot; |
| LATENCY_SENSITIVE | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE&quot; |
| LATENCY_TOLERANT | &quot;PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT&quot; |



