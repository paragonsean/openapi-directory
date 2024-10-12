# AmazonSageMakerService.CreateNotebookInstanceInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notebookInstanceName** | **String** |  | 
**instanceType** | [**InstanceType**](InstanceType.md) |  | 
**subnetId** | **String** |  | [optional] 
**securityGroupIds** | **Array** |  | [optional] 
**roleArn** | **String** |  | 
**kmsKeyId** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 
**lifecycleConfigName** | **String** |  | [optional] 
**directInternetAccess** | [**DirectInternetAccess**](DirectInternetAccess.md) |  | [optional] 
**volumeSizeInGB** | **Number** |  | [optional] 
**acceleratorTypes** | **Array** |  | [optional] 
**defaultCodeRepository** | **String** |  | [optional] 
**additionalCodeRepositories** | **Array** |  | [optional] 
**rootAccess** | [**RootAccess**](RootAccess.md) |  | [optional] 
**platformIdentifier** | **String** |  | [optional] 
**instanceMetadataServiceConfiguration** | [**CreateNotebookInstanceInputInstanceMetadataServiceConfiguration**](CreateNotebookInstanceInputInstanceMetadataServiceConfiguration.md) |  | [optional] 


