# SiteRecoveryManagementClient.A2AProtectedManagedDiskDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataPendingAtSourceAgentInMB** | **Number** | The data pending at source virtual machine in MB. | [optional] 
**dataPendingInStagingStorageAccountInMB** | **Number** | The data pending for replication in MB at staging account. | [optional] 
**dekKeyVaultArmId** | **String** | The KeyVault resource id for secret (BEK). | [optional] 
**diskCapacityInBytes** | **Number** | The disk capacity in bytes. | [optional] 
**diskId** | **String** | The managed disk Arm id. | [optional] 
**diskName** | **String** | The disk name. | [optional] 
**diskType** | **String** | The type of disk. | [optional] 
**isDiskEncrypted** | **Boolean** | A value indicating whether vm has encrypted os disk or not. | [optional] 
**isDiskKeyEncrypted** | **Boolean** | A value indicating whether disk key got encrypted or not. | [optional] 
**kekKeyVaultArmId** | **String** | The KeyVault resource id for key (KEK). | [optional] 
**keyIdentifier** | **String** | The key URL / identifier (KEK). | [optional] 
**monitoringJobType** | **String** | The type of the monitoring job. The progress is contained in MonitoringPercentageCompletion property. | [optional] 
**monitoringPercentageCompletion** | **Number** | The percentage of the monitoring job. The type of the monitoring job is defined by MonitoringJobType property. | [optional] 
**primaryStagingAzureStorageAccountId** | **String** | The primary staging storage account. | [optional] 
**recoveryReplicaDiskAccountType** | **String** | The replica disk type. Its an optional value and will be same as source disk type if not user provided. | [optional] 
**recoveryReplicaDiskId** | **String** | Recovery replica disk Arm Id. | [optional] 
**recoveryResourceGroupId** | **String** | The recovery disk resource group Arm Id. | [optional] 
**recoveryTargetDiskAccountType** | **String** | The target disk type after failover. Its an optional value and will be same as source disk type if not user provided. | [optional] 
**recoveryTargetDiskId** | **String** | Recovery target disk Arm Id. | [optional] 
**resyncRequired** | **Boolean** | A value indicating whether resync is required for this disk. | [optional] 
**secretIdentifier** | **String** | The secret URL / identifier (BEK). | [optional] 


