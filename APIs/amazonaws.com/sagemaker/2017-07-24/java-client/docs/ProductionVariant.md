

# ProductionVariant

 Identifies a model that you want to host and the resources chosen to deploy for hosting it. If you are deploying multiple models, tell SageMaker how to distribute traffic among the models by specifying variant weights. For more information on production variants, check <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html\"> Production variants</a>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**variantName** | [**String**](String.md) |  |  |
|**modelName** | [**String**](String.md) |  |  |
|**initialInstanceCount** | [**Integer**](Integer.md) |  |  [optional] |
|**instanceType** | [**ProductionVariantInstanceType**](ProductionVariantInstanceType.md) |  |  [optional] |
|**initialVariantWeight** | [**Float**](Float.md) |  |  [optional] |
|**acceleratorType** | [**ProductionVariantAcceleratorType**](ProductionVariantAcceleratorType.md) |  |  [optional] |
|**coreDumpConfig** | [**ProductionVariantCoreDumpConfig**](ProductionVariantCoreDumpConfig.md) |  |  [optional] |
|**serverlessConfig** | [**ProductionVariantServerlessConfig**](ProductionVariantServerlessConfig.md) |  |  [optional] |
|**volumeSizeInGB** | [**Integer**](Integer.md) |  |  [optional] |
|**modelDataDownloadTimeoutInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**containerStartupHealthCheckTimeoutInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**enableSSMAccess** | [**Boolean**](Boolean.md) |  |  [optional] |



