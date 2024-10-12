

# ProductionVariantSummary

Describes weight and capacities for a production variant associated with an endpoint. If you sent a request to the <code>UpdateEndpointWeightsAndCapacities</code> API and the endpoint status is <code>Updating</code>, you get different desired and current values. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**variantName** | [**String**](String.md) |  |  |
|**deployedImages** | [**List**](List.md) |  |  [optional] |
|**currentWeight** | [**Float**](Float.md) |  |  [optional] |
|**desiredWeight** | [**Float**](Float.md) |  |  [optional] |
|**currentInstanceCount** | [**Integer**](Integer.md) |  |  [optional] |
|**desiredInstanceCount** | [**Integer**](Integer.md) |  |  [optional] |
|**variantStatus** | [**List**](List.md) |  |  [optional] |
|**currentServerlessConfig** | [**PendingProductionVariantSummaryCurrentServerlessConfig**](PendingProductionVariantSummaryCurrentServerlessConfig.md) |  |  [optional] |
|**desiredServerlessConfig** | [**ProductionVariantSummaryDesiredServerlessConfig**](ProductionVariantSummaryDesiredServerlessConfig.md) |  |  [optional] |



