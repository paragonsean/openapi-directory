

# BackupInfo

Holds information for a backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupDataVersion** | **String** | Version of the backup data. |  [optional] [readonly] |
|**backupId** | **String** | Unique GUID for the backup. |  [optional] [readonly] |
|**createdDateTime** | **OffsetDateTime** | Creation time of the backup. |  [optional] [readonly] |
|**deploymentID** | **String** | Deployment Id of the stamp. |  [optional] [readonly] |
|**oemVersion** | **String** | OEM version. |  [optional] [readonly] |
|**roleStatus** | [**List&lt;RoleOperationStatus&gt;**](RoleOperationStatus.md) | object |  [optional] |
|**stampVersion** | **String** | Current version. |  [optional] [readonly] |
|**status** | **OperationStatus** |  |  [optional] |
|**timeTakenToCreate** | **String** | Duration to create the backup. |  [optional] [readonly] |



