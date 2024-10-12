

# DescribeInferenceRecommendationsJobResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobName** | [**String**](String.md) |  |  |
|**jobDescription** | [**String**](String.md) |  |  [optional] |
|**jobType** | [**RecommendationJobType**](RecommendationJobType.md) |  |  |
|**jobArn** | [**String**](String.md) |  |  |
|**roleArn** | [**String**](String.md) |  |  |
|**status** | [**RecommendationJobStatus**](RecommendationJobStatus.md) |  |  |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**completionTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**inputConfig** | [**DescribeInferenceRecommendationsJobResponseInputConfig**](DescribeInferenceRecommendationsJobResponseInputConfig.md) |  |  |
|**stoppingConditions** | [**DescribeInferenceRecommendationsJobResponseStoppingConditions**](DescribeInferenceRecommendationsJobResponseStoppingConditions.md) |  |  [optional] |
|**inferenceRecommendations** | [**List**](List.md) |  |  [optional] |
|**endpointPerformances** | [**List**](List.md) |  |  [optional] |



