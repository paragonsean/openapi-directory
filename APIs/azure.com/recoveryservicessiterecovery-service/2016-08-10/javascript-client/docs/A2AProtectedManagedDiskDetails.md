# SiteRecoveryManagementClient.A2AProtectedManagedDiskDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataPendingAtSourceAgentInMB** | **Number** | The data pending at source virtual machine in MB. | [optional] 
**dataPendingInStagingStorageAccountInMB** | **Number** | The data pending for replication in MB at staging account. | [optional] 
**diskCapacityInBytes** | **Number** | The disk capacity in bytes. | [optional] 
**diskId** | **String** | The managed disk Arm id. | [optional] 
**diskName** | **String** | The disk name. | [optional] 
**diskType** | **String** | The type of disk. | [optional] 
**monitoringJobType** | **String** | The type of the monitoring job. The progress is contained in MonitoringPercentageCompletion property. | [optional] 
**monitoringPercentageCompletion** | **Number** | The percentage of the monitoring job. The type of the monitoring job is defined by MonitoringJobType property. | [optional] 
**primaryStagingAzureStorageAccountId** | **String** | The primary staging storage account. | [optional] 
**recoveryAzureResourceGroupId** | **String** | The recovery disk resource group Arm Id. | [optional] 
**recoveryDiskId** | **String** | Recovery disk Arm Id. | [optional] 
**resyncRequired** | **Boolean** | A value indicating whether resync is required for this disk. | [optional] 


