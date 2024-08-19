# AmazonSageMakerService.CreateModelPackageInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modelPackageName** | **String** |  | [optional] 
**modelPackageGroupName** | **String** |  | [optional] 
**modelPackageDescription** | **String** |  | [optional] 
**inferenceSpecification** | [**CreateModelPackageInputInferenceSpecification**](CreateModelPackageInputInferenceSpecification.md) |  | [optional] 
**validationSpecification** | [**CreateModelPackageInputValidationSpecification**](CreateModelPackageInputValidationSpecification.md) |  | [optional] 
**sourceAlgorithmSpecification** | [**CreateModelPackageInputSourceAlgorithmSpecification**](CreateModelPackageInputSourceAlgorithmSpecification.md) |  | [optional] 
**certifyForMarketplace** | **Boolean** |  | [optional] 
**tags** | **Array** |  | [optional] 
**modelApprovalStatus** | [**ModelApprovalStatus**](ModelApprovalStatus.md) |  | [optional] 
**metadataProperties** | [**MetadataProperties**](MetadataProperties.md) |  | [optional] 
**modelMetrics** | [**CreateModelPackageInputModelMetrics**](CreateModelPackageInputModelMetrics.md) |  | [optional] 
**clientToken** | **String** |  | [optional] 
**customerMetadataProperties** | **Object** |  | [optional] 
**driftCheckBaselines** | [**CreateModelPackageInputDriftCheckBaselines**](CreateModelPackageInputDriftCheckBaselines.md) |  | [optional] 
**domain** | **String** |  | [optional] 
**task** | **String** |  | [optional] 
**samplePayloadUrl** | **String** |  | [optional] 
**additionalInferenceSpecifications** | **Array** |  | [optional] 


