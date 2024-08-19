# AmazonSageMakerService.DescribeInferenceRecommendationsJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobName** | **String** |  | 
**jobDescription** | **String** |  | [optional] 
**jobType** | [**RecommendationJobType**](RecommendationJobType.md) |  | 
**jobArn** | **String** |  | 
**roleArn** | **String** |  | 
**status** | [**RecommendationJobStatus**](RecommendationJobStatus.md) |  | 
**creationTime** | **Date** |  | 
**completionTime** | **Date** |  | [optional] 
**lastModifiedTime** | **Date** |  | 
**failureReason** | **String** |  | [optional] 
**inputConfig** | [**DescribeInferenceRecommendationsJobResponseInputConfig**](DescribeInferenceRecommendationsJobResponseInputConfig.md) |  | 
**stoppingConditions** | [**DescribeInferenceRecommendationsJobResponseStoppingConditions**](DescribeInferenceRecommendationsJobResponseStoppingConditions.md) |  | [optional] 
**inferenceRecommendations** | **Array** |  | [optional] 
**endpointPerformances** | **Array** |  | [optional] 


