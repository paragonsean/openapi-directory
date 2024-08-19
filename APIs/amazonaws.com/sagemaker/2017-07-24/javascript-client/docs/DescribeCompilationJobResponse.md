# AmazonSageMakerService.DescribeCompilationJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compilationJobName** | **String** |  | 
**compilationJobArn** | **String** |  | 
**compilationJobStatus** | [**CompilationJobStatus**](CompilationJobStatus.md) |  | 
**compilationStartTime** | **Date** |  | [optional] 
**compilationEndTime** | **Date** |  | [optional] 
**stoppingCondition** | [**CreateCompilationJobRequestStoppingCondition**](CreateCompilationJobRequestStoppingCondition.md) |  | 
**inferenceImage** | **String** |  | [optional] 
**modelPackageVersionArn** | **String** |  | [optional] 
**creationTime** | **Date** |  | 
**lastModifiedTime** | **Date** |  | 
**failureReason** | **String** |  | 
**modelArtifacts** | [**DescribeCompilationJobResponseModelArtifacts**](DescribeCompilationJobResponseModelArtifacts.md) |  | 
**modelDigests** | [**DescribeCompilationJobResponseModelDigests**](DescribeCompilationJobResponseModelDigests.md) |  | [optional] 
**roleArn** | **String** |  | 
**inputConfig** | [**DescribeCompilationJobResponseInputConfig**](DescribeCompilationJobResponseInputConfig.md) |  | 
**outputConfig** | [**DescribeCompilationJobResponseOutputConfig**](DescribeCompilationJobResponseOutputConfig.md) |  | 
**vpcConfig** | [**CreateCompilationJobRequestVpcConfig**](CreateCompilationJobRequestVpcConfig.md) |  | [optional] 


