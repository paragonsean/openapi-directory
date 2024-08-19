

# DescribeModelPackageOutput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**modelPackageName** | [**String**](String.md) |  |  |
|**modelPackageGroupName** | [**String**](String.md) |  |  [optional] |
|**modelPackageVersion** | [**Integer**](Integer.md) |  |  [optional] |
|**modelPackageArn** | [**String**](String.md) |  |  |
|**modelPackageDescription** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**inferenceSpecification** | [**DescribeModelPackageOutputInferenceSpecification**](DescribeModelPackageOutputInferenceSpecification.md) |  |  [optional] |
|**sourceAlgorithmSpecification** | [**CreateModelPackageInputSourceAlgorithmSpecification**](CreateModelPackageInputSourceAlgorithmSpecification.md) |  |  [optional] |
|**validationSpecification** | [**DescribeModelPackageOutputValidationSpecification**](DescribeModelPackageOutputValidationSpecification.md) |  |  [optional] |
|**modelPackageStatus** | [**ModelPackageStatus**](ModelPackageStatus.md) |  |  |
|**modelPackageStatusDetails** | [**DescribeModelPackageOutputModelPackageStatusDetails**](DescribeModelPackageOutputModelPackageStatusDetails.md) |  |  |
|**certifyForMarketplace** | [**Boolean**](Boolean.md) |  |  [optional] |
|**modelApprovalStatus** | [**ModelApprovalStatus**](ModelApprovalStatus.md) |  |  [optional] |
|**createdBy** | [**UserContext**](UserContext.md) |  |  [optional] |
|**metadataProperties** | [**MetadataProperties**](MetadataProperties.md) |  |  [optional] |
|**modelMetrics** | [**DescribeModelPackageOutputModelMetrics**](DescribeModelPackageOutputModelMetrics.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedBy** | [**UserContext**](UserContext.md) |  |  [optional] |
|**approvalDescription** | [**String**](String.md) |  |  [optional] |
|**customerMetadataProperties** | [**Map**](Map.md) |  |  [optional] |
|**driftCheckBaselines** | [**CreateModelPackageInputDriftCheckBaselines**](CreateModelPackageInputDriftCheckBaselines.md) |  |  [optional] |
|**domain** | [**String**](String.md) |  |  [optional] |
|**task** | [**String**](String.md) |  |  [optional] |
|**samplePayloadUrl** | [**String**](String.md) |  |  [optional] |
|**additionalInferenceSpecifications** | [**List**](List.md) |  |  [optional] |



