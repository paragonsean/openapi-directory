# AmazonLookoutForEquipment.CreateModelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modelName** | **String** |  | 
**datasetName** | **String** |  | 
**datasetSchema** | [**CreateModelRequestDatasetSchema**](CreateModelRequestDatasetSchema.md) |  | [optional] 
**labelsInputConfiguration** | [**CreateModelRequestLabelsInputConfiguration**](CreateModelRequestLabelsInputConfiguration.md) |  | [optional] 
**clientToken** | **String** |  | 
**trainingDataStartTime** | **Date** |  | [optional] 
**trainingDataEndTime** | **Date** |  | [optional] 
**evaluationDataStartTime** | **Date** |  | [optional] 
**evaluationDataEndTime** | **Date** |  | [optional] 
**roleArn** | **String** |  | [optional] 
**dataPreProcessingConfiguration** | [**CreateModelRequestDataPreProcessingConfiguration**](CreateModelRequestDataPreProcessingConfiguration.md) |  | [optional] 
**serverSideKmsKeyId** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 
**offCondition** | **String** |  | [optional] 


