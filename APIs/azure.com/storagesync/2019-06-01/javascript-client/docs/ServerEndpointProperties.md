# MicrosoftStorageSync.ServerEndpointProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudTiering** | [**FeatureStatus**](FeatureStatus.md) |  | [optional] 
**cloudTieringStatus** | [**ServerEndpointCloudTieringStatus**](ServerEndpointCloudTieringStatus.md) |  | [optional] 
**friendlyName** | **String** | Friendly Name | [optional] 
**lastOperationName** | **String** | Resource Last Operation Name | [optional] [readonly] 
**lastWorkflowId** | **String** | ServerEndpoint lastWorkflowId | [optional] [readonly] 
**offlineDataTransfer** | [**FeatureStatus**](FeatureStatus.md) |  | [optional] 
**offlineDataTransferShareName** | **String** | Offline data transfer share name | [optional] 
**offlineDataTransferStorageAccountResourceId** | **String** | Offline data transfer storage account resource ID | [optional] [readonly] 
**offlineDataTransferStorageAccountTenantId** | **String** | Offline data transfer storage account tenant ID | [optional] [readonly] 
**provisioningState** | **String** | ServerEndpoint Provisioning State | [optional] [readonly] 
**recallStatus** | [**ServerEndpointRecallStatus**](ServerEndpointRecallStatus.md) |  | [optional] 
**serverLocalPath** | **String** | Server folder used for data synchronization | [optional] 
**serverResourceId** | **String** | Arm resource identifier. | [optional] 
**syncStatus** | [**ServerEndpointSyncStatus**](ServerEndpointSyncStatus.md) |  | [optional] 
**tierFilesOlderThanDays** | **Number** | Tier files older than days. | [optional] 
**volumeFreeSpacePercent** | **Number** | Level of free space to be maintained by Cloud Tiering if it is enabled. | [optional] 


