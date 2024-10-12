# BackupManagementClient.BackupInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupDataVersion** | **String** | Version of the backup data. | [optional] [readonly] 
**createdDateTime** | **Date** | Creation time of the backup. | [optional] [readonly] 
**deploymentID** | **String** | Deployment Id of the stamp. | [optional] [readonly] 
**encryptionCertThumbprint** | **String** | The thumbprint of the certificate used to encrypt the backup encryption key. | [optional] [readonly] 
**isCloudRecoveryReady** | **Boolean** | True if the backup can be used for cloud recovery scenario. | [optional] [readonly] 
**oemVersion** | **String** | OEM version. | [optional] [readonly] 
**roleStatus** | [**[RoleOperationStatus]**](RoleOperationStatus.md) | object | [optional] 
**stampVersion** | **String** | Azure Stack stamp version of the backup. | [optional] [readonly] 
**status** | [**OperationStatus**](OperationStatus.md) |  | [optional] 
**timeTakenToCreate** | **String** | Duration to create the backup. | [optional] [readonly] 


