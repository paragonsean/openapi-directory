

# ModelPackage

A versioned model that can be deployed for SageMaker inference.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**modelPackageName** | [**String**](String.md) |  |  [optional] |
|**modelPackageGroupName** | [**String**](String.md) |  |  [optional] |
|**modelPackageVersion** | [**Integer**](Integer.md) |  |  [optional] |
|**modelPackageArn** | [**String**](String.md) |  |  [optional] |
|**modelPackageDescription** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**inferenceSpecification** | [**ModelPackageInferenceSpecification**](ModelPackageInferenceSpecification.md) |  |  [optional] |
|**sourceAlgorithmSpecification** | [**ModelPackageSourceAlgorithmSpecification**](ModelPackageSourceAlgorithmSpecification.md) |  |  [optional] |
|**validationSpecification** | [**ModelPackageValidationSpecification**](ModelPackageValidationSpecification.md) |  |  [optional] |
|**modelPackageStatus** | [**ModelPackageStatus**](ModelPackageStatus.md) |  |  [optional] |
|**modelPackageStatusDetails** | [**ModelPackageModelPackageStatusDetails**](ModelPackageModelPackageStatusDetails.md) |  |  [optional] |
|**certifyForMarketplace** | [**Boolean**](Boolean.md) |  |  [optional] |
|**modelApprovalStatus** | [**ModelApprovalStatus**](ModelApprovalStatus.md) |  |  [optional] |
|**createdBy** | [**ModelPackageCreatedBy**](ModelPackageCreatedBy.md) |  |  [optional] |
|**metadataProperties** | [**ModelPackageMetadataProperties**](ModelPackageMetadataProperties.md) |  |  [optional] |
|**modelMetrics** | [**DescribeModelPackageOutputModelMetrics**](DescribeModelPackageOutputModelMetrics.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedBy** | [**ModelPackageCreatedBy**](ModelPackageCreatedBy.md) |  |  [optional] |
|**approvalDescription** | [**String**](String.md) |  |  [optional] |
|**domain** | [**String**](String.md) |  |  [optional] |
|**task** | [**String**](String.md) |  |  [optional] |
|**samplePayloadUrl** | [**String**](String.md) |  |  [optional] |
|**additionalInferenceSpecifications** | [**List**](List.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**customerMetadataProperties** | [**Map**](Map.md) |  |  [optional] |
|**driftCheckBaselines** | [**ModelPackageDriftCheckBaselines**](ModelPackageDriftCheckBaselines.md) |  |  [optional] |



