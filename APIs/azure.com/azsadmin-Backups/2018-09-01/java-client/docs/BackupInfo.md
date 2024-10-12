

# BackupInfo

Holds information for a backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupDataVersion** | **String** | Version of the backup data. |  [optional] [readonly] |
|**createdDateTime** | **OffsetDateTime** | Creation time of the backup. |  [optional] [readonly] |
|**deploymentID** | **String** | Deployment Id of the stamp. |  [optional] [readonly] |
|**encryptionCertThumbprint** | **String** | The thumbprint of the certificate used to encrypt the backup encryption key. |  [optional] [readonly] |
|**isCloudRecoveryReady** | **Boolean** | True if the backup can be used for cloud recovery scenario. |  [optional] [readonly] |
|**oemVersion** | **String** | OEM version. |  [optional] [readonly] |
|**roleStatus** | [**List&lt;RoleOperationStatus&gt;**](RoleOperationStatus.md) | object |  [optional] |
|**stampVersion** | **String** | Azure Stack stamp version of the backup. |  [optional] [readonly] |
|**status** | **OperationStatus** |  |  [optional] |
|**timeTakenToCreate** | **String** | Duration to create the backup. |  [optional] [readonly] |



