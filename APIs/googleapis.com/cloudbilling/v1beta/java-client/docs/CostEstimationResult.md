

# CostEstimationResult

The result of a estimating the costs of a `CostScenario`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | Required. The ISO 4217 currency code for the cost estimate. |  [optional] |
|**segmentCostEstimates** | [**List&lt;SegmentCostEstimate&gt;**](SegmentCostEstimate.md) | Required. Estimated costs for each idealized month of a &#x60;CostScenario&#x60;. |  [optional] |
|**skus** | [**List&lt;Sku&gt;**](Sku.md) | Required. Information about SKUs used in the estimate. |  [optional] |



