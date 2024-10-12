

# A2AProtectedDiskDetails

A2A protected disk details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataPendingAtSourceAgentInMB** | **Double** | The data pending at source virtual machine in MB. |  [optional] |
|**dataPendingInStagingStorageAccountInMB** | **Double** | The data pending for replication in MB at staging account. |  [optional] |
|**diskCapacityInBytes** | **Long** | The disk capacity in bytes. |  [optional] |
|**diskName** | **String** | The disk name. |  [optional] |
|**diskType** | **String** | The type of disk. |  [optional] |
|**diskUri** | **String** | The disk uri. |  [optional] |
|**monitoringJobType** | **String** | The type of the monitoring job. The progress is contained in MonitoringPercentageCompletion property. |  [optional] |
|**monitoringPercentageCompletion** | **Integer** | The percentage of the monitoring job. The type of the monitoring job is defined by MonitoringJobType property. |  [optional] |
|**primaryDiskAzureStorageAccountId** | **String** | The primary disk storage account. |  [optional] |
|**primaryStagingAzureStorageAccountId** | **String** | The primary staging storage account. |  [optional] |
|**recoveryAzureStorageAccountId** | **String** | The recovery disk storage account. |  [optional] |
|**recoveryDiskUri** | **String** | Recovery disk uri. |  [optional] |
|**resyncRequired** | **Boolean** | A value indicating whether resync is required for this disk. |  [optional] |



