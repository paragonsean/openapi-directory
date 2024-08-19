

# DescribeCompilationJobResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compilationJobName** | [**String**](String.md) |  |  |
|**compilationJobArn** | [**String**](String.md) |  |  |
|**compilationJobStatus** | [**CompilationJobStatus**](CompilationJobStatus.md) |  |  |
|**compilationStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**compilationEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**stoppingCondition** | [**CreateCompilationJobRequestStoppingCondition**](CreateCompilationJobRequestStoppingCondition.md) |  |  |
|**inferenceImage** | [**String**](String.md) |  |  [optional] |
|**modelPackageVersionArn** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**failureReason** | [**String**](String.md) |  |  |
|**modelArtifacts** | [**DescribeCompilationJobResponseModelArtifacts**](DescribeCompilationJobResponseModelArtifacts.md) |  |  |
|**modelDigests** | [**DescribeCompilationJobResponseModelDigests**](DescribeCompilationJobResponseModelDigests.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  |
|**inputConfig** | [**DescribeCompilationJobResponseInputConfig**](DescribeCompilationJobResponseInputConfig.md) |  |  |
|**outputConfig** | [**DescribeCompilationJobResponseOutputConfig**](DescribeCompilationJobResponseOutputConfig.md) |  |  |
|**vpcConfig** | [**CreateCompilationJobRequestVpcConfig**](CreateCompilationJobRequestVpcConfig.md) |  |  [optional] |



