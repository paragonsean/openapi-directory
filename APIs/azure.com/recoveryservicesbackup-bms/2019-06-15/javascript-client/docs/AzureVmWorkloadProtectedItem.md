# RecoveryServicesBackupClient.AzureVmWorkloadProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extendedInfo** | [**AzureVmWorkloadProtectedItemExtendedInfo**](AzureVmWorkloadProtectedItemExtendedInfo.md) |  | [optional] 
**friendlyName** | **String** | Friendly name of the DB represented by this backup item. | [optional] 
**lastBackupErrorDetail** | [**ErrorDetail**](ErrorDetail.md) |  | [optional] 
**lastBackupStatus** | **String** | Last backup operation status. Possible values: Healthy, Unhealthy. | [optional] 
**lastBackupTime** | **Date** | Timestamp of the last backup operation on this backup item. | [optional] 
**parentName** | **String** | Parent name of the DB such as Instance or Availability Group. | [optional] 
**parentType** | **String** | Parent type of protected item, example: for a DB, standalone server or distributed | [optional] 
**protectedItemDataSourceId** | **String** | Data ID of the protected item. | [optional] 
**protectedItemHealthStatus** | **String** | Health status of the backup item, evaluated based on last heartbeat received | [optional] 
**protectionState** | **String** | Backup state of this backup item. | [optional] 
**protectionStatus** | **String** | Backup status of this backup item. | [optional] 
**serverName** | **String** | Host/Cluster Name for instance or AG | [optional] 



## Enum: LastBackupStatusEnum


* `Invalid` (value: `"Invalid"`)

* `Healthy` (value: `"Healthy"`)

* `Unhealthy` (value: `"Unhealthy"`)

* `IRPending` (value: `"IRPending"`)





## Enum: ProtectedItemHealthStatusEnum


* `Invalid` (value: `"Invalid"`)

* `Healthy` (value: `"Healthy"`)

* `Unhealthy` (value: `"Unhealthy"`)

* `NotReachable` (value: `"NotReachable"`)

* `IRPending` (value: `"IRPending"`)





## Enum: ProtectionStateEnum


* `Invalid` (value: `"Invalid"`)

* `IRPending` (value: `"IRPending"`)

* `Protected` (value: `"Protected"`)

* `ProtectionError` (value: `"ProtectionError"`)

* `ProtectionStopped` (value: `"ProtectionStopped"`)

* `ProtectionPaused` (value: `"ProtectionPaused"`)




