# SiteRecoveryManagementClient.A2AEnableProtectionInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskEncryptionInfo** | [**DiskEncryptionInfo**](DiskEncryptionInfo.md) |  | [optional] 
**fabricObjectId** | **String** | The fabric specific object Id of the virtual machine. | [optional] 
**multiVmGroupName** | **String** | The multi vm group name. | [optional] 
**recoveryAvailabilitySetId** | **String** | The recovery availability set Id. | [optional] 
**recoveryBootDiagStorageAccountId** | **String** | The boot diagnostic storage account. | [optional] 
**recoveryCloudServiceId** | **String** | The recovery cloud service Id. Valid for V1 scenarios. | [optional] 
**recoveryContainerId** | **String** | The recovery container Id. | [optional] 
**recoveryResourceGroupId** | **String** | The recovery resource group Id. Valid for V2 scenarios. | [optional] 
**vmDisks** | [**[A2AVmDiskInputDetails]**](A2AVmDiskInputDetails.md) | The list of vm disk details. | [optional] 
**vmManagedDisks** | [**[A2AVmManagedDiskInputDetails]**](A2AVmManagedDiskInputDetails.md) | The list of vm managed disk details. | [optional] 


