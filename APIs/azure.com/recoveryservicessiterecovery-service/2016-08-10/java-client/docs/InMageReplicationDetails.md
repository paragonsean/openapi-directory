

# InMageReplicationDetails

InMage provider specific settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeSiteType** | **String** | The active location of the VM. If the VM is being protected from Azure, this field will take values from { Azure, OnPrem }. If the VM is being protected between two data-centers, this field will be OnPrem always. |  [optional] |
|**agentDetails** | [**InMageAgentDetails**](InMageAgentDetails.md) |  |  [optional] |
|**azureStorageAccountId** | **String** | A value indicating the underlying Azure storage account. If the VM is not running in Azure, this value shall be set to null. |  [optional] |
|**compressedDataRateInMB** | **Double** | The compressed data change rate in MB. |  [optional] |
|**consistencyPoints** | **Map&lt;String, OffsetDateTime&gt;** | The collection of Consistency points. |  [optional] |
|**datastores** | **List&lt;String&gt;** | The data stores of the on-premise machine Value can be list of strings that contain data store names |  [optional] |
|**discoveryType** | **String** | A value indicating the discovery type of the machine. |  [optional] |
|**diskResized** | **String** | A value indicating whether any disk is resized for this VM. |  [optional] |
|**infrastructureVmId** | **String** | The infrastructure VM Id. |  [optional] |
|**ipAddress** | **String** | The source IP address. |  [optional] |
|**lastHeartbeat** | **OffsetDateTime** | The last heartbeat received from the source server. |  [optional] |
|**lastRpoCalculatedTime** | **OffsetDateTime** | The last RPO calculated time. |  [optional] |
|**lastUpdateReceivedTime** | **OffsetDateTime** | The last update time received from on-prem components. |  [optional] |
|**masterTargetId** | **String** | The master target Id. |  [optional] |
|**multiVmGroupId** | **String** | The multi vm group Id, if any. |  [optional] |
|**multiVmGroupName** | **String** | The multi vm group name, if any. |  [optional] |
|**multiVmSyncStatus** | **String** | A value indicating whether the multi vm sync is enabled or disabled. |  [optional] |
|**osDetails** | [**OSDiskDetails**](OSDiskDetails.md) |  |  [optional] |
|**osVersion** | **String** | The OS Version of the protected item. |  [optional] |
|**processServerId** | **String** | The process server Id. |  [optional] |
|**protectedDisks** | [**List&lt;InMageProtectedDiskDetails&gt;**](InMageProtectedDiskDetails.md) | The list of protected disks. |  [optional] |
|**protectionStage** | **String** | The protection stage. |  [optional] |
|**rebootAfterUpdateStatus** | **String** | A value indicating whether the source server requires a restart after update. |  [optional] |
|**replicaId** | **String** | The replica id of the protected item. |  [optional] |
|**resyncDetails** | [**InitialReplicationDetails**](InitialReplicationDetails.md) |  |  [optional] |
|**retentionWindowEnd** | **OffsetDateTime** | The retention window end time. |  [optional] |
|**retentionWindowStart** | **OffsetDateTime** | The retention window start time. |  [optional] |
|**rpoInSeconds** | **Long** | The RPO in seconds. |  [optional] |
|**sourceVmCPUCount** | **Integer** | The CPU count of the VM on the primary side. |  [optional] |
|**sourceVmRAMSizeInMB** | **Integer** | The RAM size of the VM on the primary side. |  [optional] |
|**uncompressedDataRateInMB** | **Double** | The uncompressed data change rate in MB. |  [optional] |
|**vCenterInfrastructureId** | **String** | The vCenter infrastructure Id. |  [optional] |
|**validationErrors** | [**List&lt;HealthError&gt;**](HealthError.md) | The validation errors of the on-premise machine Value can be list of validation errors |  [optional] |
|**vmId** | **String** | The virtual machine Id. |  [optional] |
|**vmNics** | [**List&lt;VMNicDetails&gt;**](VMNicDetails.md) | The PE Network details. |  [optional] |
|**vmProtectionState** | **String** | The protection state for the vm. |  [optional] |
|**vmProtectionStateDescription** | **String** | The protection state description for the vm. |  [optional] |



