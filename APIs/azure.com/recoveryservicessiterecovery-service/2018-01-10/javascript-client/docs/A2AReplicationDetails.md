# SiteRecoveryManagementClient.A2AReplicationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentVersion** | **String** | The agent version. | [optional] 
**fabricObjectId** | **String** | The fabric specific object Id of the virtual machine. | [optional] 
**isReplicationAgentUpdateRequired** | **Boolean** | A value indicating whether replication agent update is required. | [optional] 
**lastHeartbeat** | **Date** | The last heartbeat received from the source server. | [optional] 
**lastRpoCalculatedTime** | **Date** | The time (in UTC) when the last RPO value was calculated by Protection Service. | [optional] 
**lifecycleId** | **String** | An id associated with the PE that survives actions like switch protection which change the backing PE/CPE objects internally.The lifecycle id gets carried forward to have a link/continuity in being able to have an Id that denotes the \&quot;same\&quot; protected item even though other internal Ids/ARM Id might be changing. | [optional] 
**managementId** | **String** | The management Id. | [optional] 
**monitoringJobType** | **String** | The type of the monitoring job. The progress is contained in MonitoringPercentageCompletion property. | [optional] 
**monitoringPercentageCompletion** | **Number** | The percentage of the monitoring job. The type of the monitoring job is defined by MonitoringJobType property. | [optional] 
**multiVmGroupCreateOption** | **String** | Whether Multi VM group is auto created or specified by user. | [optional] 
**multiVmGroupId** | **String** | The multi vm group Id. | [optional] 
**multiVmGroupName** | **String** | The multi vm group name. | [optional] 
**osType** | **String** | The type of operating system. | [optional] 
**primaryFabricLocation** | **String** | Primary fabric location. | [optional] 
**protectedDisks** | [**[A2AProtectedDiskDetails]**](A2AProtectedDiskDetails.md) | The list of protected disks. | [optional] 
**protectedManagedDisks** | [**[A2AProtectedManagedDiskDetails]**](A2AProtectedManagedDiskDetails.md) | The list of protected managed disks. | [optional] 
**recoveryAvailabilitySet** | **String** | The recovery availability set. | [optional] 
**recoveryAzureResourceGroupId** | **String** | The recovery resource group. | [optional] 
**recoveryAzureVMName** | **String** | The name of recovery virtual machine. | [optional] 
**recoveryAzureVMSize** | **String** | The size of recovery virtual machine. | [optional] 
**recoveryBootDiagStorageAccountId** | **String** | The recovery boot diagnostic storage account Arm Id. | [optional] 
**recoveryCloudService** | **String** | The recovery cloud service. | [optional] 
**recoveryFabricLocation** | **String** | The recovery fabric location. | [optional] 
**recoveryFabricObjectId** | **String** | The recovery fabric object Id. | [optional] 
**rpoInSeconds** | **Number** | The last RPO value in seconds. | [optional] 
**selectedRecoveryAzureNetworkId** | **String** | The recovery virtual network. | [optional] 
**testFailoverRecoveryFabricObjectId** | **String** | The test failover fabric object Id. | [optional] 
**vmNics** | [**[VMNicDetails]**](VMNicDetails.md) | The virtual machine nic details. | [optional] 
**vmProtectionState** | **String** | The protection state for the vm. | [optional] 
**vmProtectionStateDescription** | **String** | The protection state description for the vm. | [optional] 
**vmSyncedConfigDetails** | [**AzureToAzureVmSyncedConfigDetails**](AzureToAzureVmSyncedConfigDetails.md) |  | [optional] 



## Enum: MultiVmGroupCreateOptionEnum


* `AutoCreated` (value: `"AutoCreated"`)

* `UserSpecified` (value: `"UserSpecified"`)




