

# RecommendationJobContainerConfig

Specifies mandatory fields for running an Inference Recommender job directly in the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html\">CreateInferenceRecommendationsJob</a> API. The fields specified in <code>ContainerConfig</code> override the corresponding fields in the model package. Use <code>ContainerConfig</code> if you want to specify these fields for the recommendation job but don't want to edit them in your model package.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | [**String**](String.md) |  |  [optional] |
|**task** | [**String**](String.md) |  |  [optional] |
|**framework** | [**String**](String.md) |  |  [optional] |
|**frameworkVersion** | [**String**](String.md) |  |  [optional] |
|**payloadConfig** | [**RecommendationJobContainerConfigPayloadConfig**](RecommendationJobContainerConfigPayloadConfig.md) |  |  [optional] |
|**nearestModelName** | [**String**](String.md) |  |  [optional] |
|**supportedInstanceTypes** | [**List**](List.md) |  |  [optional] |
|**dataInputConfig** | [**String**](String.md) |  |  [optional] |
|**supportedEndpointType** | [**RecommendationJobSupportedEndpointType**](RecommendationJobSupportedEndpointType.md) |  |  [optional] |



