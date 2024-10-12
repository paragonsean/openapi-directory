

# PendingProductionVariantSummary

The production variant summary for a deployment when an endpoint is creating or updating with the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html\">CreateEndpoint</a> or <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html\">UpdateEndpoint</a> operations. Describes the <code>VariantStatus </code>, weight and capacity for a production variant associated with an endpoint. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**variantName** | [**String**](String.md) |  |  |
|**deployedImages** | [**List**](List.md) |  |  [optional] |
|**currentWeight** | [**Float**](Float.md) |  |  [optional] |
|**desiredWeight** | [**Float**](Float.md) |  |  [optional] |
|**currentInstanceCount** | [**Integer**](Integer.md) |  |  [optional] |
|**desiredInstanceCount** | [**Integer**](Integer.md) |  |  [optional] |
|**instanceType** | [**ProductionVariantInstanceType**](ProductionVariantInstanceType.md) |  |  [optional] |
|**acceleratorType** | [**ProductionVariantAcceleratorType**](ProductionVariantAcceleratorType.md) |  |  [optional] |
|**variantStatus** | [**List**](List.md) |  |  [optional] |
|**currentServerlessConfig** | [**PendingProductionVariantSummaryCurrentServerlessConfig**](PendingProductionVariantSummaryCurrentServerlessConfig.md) |  |  [optional] |
|**desiredServerlessConfig** | [**PendingProductionVariantSummaryDesiredServerlessConfig**](PendingProductionVariantSummaryDesiredServerlessConfig.md) |  |  [optional] |



