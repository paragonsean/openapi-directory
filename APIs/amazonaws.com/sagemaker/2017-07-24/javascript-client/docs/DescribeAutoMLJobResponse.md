# AmazonSageMakerService.DescribeAutoMLJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoMLJobName** | **String** |  | 
**autoMLJobArn** | **String** |  | 
**inputDataConfig** | **Array** |  | 
**outputDataConfig** | [**DescribeAutoMLJobResponseOutputDataConfig**](DescribeAutoMLJobResponseOutputDataConfig.md) |  | 
**roleArn** | **String** |  | 
**autoMLJobObjective** | [**DescribeAutoMLJobResponseAutoMLJobObjective**](DescribeAutoMLJobResponseAutoMLJobObjective.md) |  | [optional] 
**problemType** | [**ProblemType**](ProblemType.md) |  | [optional] 
**autoMLJobConfig** | [**DescribeAutoMLJobResponseAutoMLJobConfig**](DescribeAutoMLJobResponseAutoMLJobConfig.md) |  | [optional] 
**creationTime** | **Date** |  | 
**endTime** | **Date** |  | [optional] 
**lastModifiedTime** | **Date** |  | 
**failureReason** | **String** |  | [optional] 
**partialFailureReasons** | **Array** |  | [optional] 
**bestCandidate** | [**DescribeAutoMLJobResponseBestCandidate**](DescribeAutoMLJobResponseBestCandidate.md) |  | [optional] 
**autoMLJobStatus** | [**AutoMLJobStatus**](AutoMLJobStatus.md) |  | 
**autoMLJobSecondaryStatus** | [**AutoMLJobSecondaryStatus**](AutoMLJobSecondaryStatus.md) |  | 
**generateCandidateDefinitionsOnly** | **Boolean** |  | [optional] 
**autoMLJobArtifacts** | [**DescribeAutoMLJobResponseAutoMLJobArtifacts**](DescribeAutoMLJobResponseAutoMLJobArtifacts.md) |  | [optional] 
**resolvedAttributes** | [**DescribeAutoMLJobResponseResolvedAttributes**](DescribeAutoMLJobResponseResolvedAttributes.md) |  | [optional] 
**modelDeployConfig** | [**DescribeAutoMLJobResponseModelDeployConfig**](DescribeAutoMLJobResponseModelDeployConfig.md) |  | [optional] 
**modelDeployResult** | [**DescribeAutoMLJobResponseModelDeployResult**](DescribeAutoMLJobResponseModelDeployResult.md) |  | [optional] 


