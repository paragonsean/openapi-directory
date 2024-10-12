# AmazonSageMakerService.DescribeModelPackageOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modelPackageName** | **String** |  | 
**modelPackageGroupName** | **String** |  | [optional] 
**modelPackageVersion** | **Number** |  | [optional] 
**modelPackageArn** | **String** |  | 
**modelPackageDescription** | **String** |  | [optional] 
**creationTime** | **Date** |  | 
**inferenceSpecification** | [**DescribeModelPackageOutputInferenceSpecification**](DescribeModelPackageOutputInferenceSpecification.md) |  | [optional] 
**sourceAlgorithmSpecification** | [**CreateModelPackageInputSourceAlgorithmSpecification**](CreateModelPackageInputSourceAlgorithmSpecification.md) |  | [optional] 
**validationSpecification** | [**DescribeModelPackageOutputValidationSpecification**](DescribeModelPackageOutputValidationSpecification.md) |  | [optional] 
**modelPackageStatus** | [**ModelPackageStatus**](ModelPackageStatus.md) |  | 
**modelPackageStatusDetails** | [**DescribeModelPackageOutputModelPackageStatusDetails**](DescribeModelPackageOutputModelPackageStatusDetails.md) |  | 
**certifyForMarketplace** | **Boolean** |  | [optional] 
**modelApprovalStatus** | [**ModelApprovalStatus**](ModelApprovalStatus.md) |  | [optional] 
**createdBy** | [**UserContext**](UserContext.md) |  | [optional] 
**metadataProperties** | [**MetadataProperties**](MetadataProperties.md) |  | [optional] 
**modelMetrics** | [**DescribeModelPackageOutputModelMetrics**](DescribeModelPackageOutputModelMetrics.md) |  | [optional] 
**lastModifiedTime** | **Date** |  | [optional] 
**lastModifiedBy** | [**UserContext**](UserContext.md) |  | [optional] 
**approvalDescription** | **String** |  | [optional] 
**customerMetadataProperties** | **Object** |  | [optional] 
**driftCheckBaselines** | [**CreateModelPackageInputDriftCheckBaselines**](CreateModelPackageInputDriftCheckBaselines.md) |  | [optional] 
**domain** | **String** |  | [optional] 
**task** | **String** |  | [optional] 
**samplePayloadUrl** | **String** |  | [optional] 
**additionalInferenceSpecifications** | **Array** |  | [optional] 


