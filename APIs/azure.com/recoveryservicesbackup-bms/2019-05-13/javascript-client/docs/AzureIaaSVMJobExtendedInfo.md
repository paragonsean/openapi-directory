# RecoveryServicesBackupClient.AzureIaaSVMJobExtendedInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamicErrorMessage** | **String** | Non localized error message on job execution. | [optional] 
**estimatedRemainingDuration** | **String** | Time remaining for execution of this job. | [optional] 
**internalPropertyBag** | **{String: String}** | Job internal properties. | [optional] 
**progressPercentage** | **Number** | Indicates progress of the job. Null if it has not started or completed. | [optional] 
**propertyBag** | **{String: String}** | Job properties. | [optional] 
**tasksList** | [**[AzureIaaSVMJobTaskDetails]**](AzureIaaSVMJobTaskDetails.md) | List of tasks associated with this job. | [optional] 


