

# IaasVMRestoreRequest

IaaS VM workload-specific restore.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affinityGroup** | **String** | Affinity group associated to VM to be restored. Used only for Classic Compute Virtual Machines. |  [optional] |
|**createNewCloudService** | **Boolean** | Should a new cloud service be created while restoring the VM. If this is false, VM will be restored to the same  cloud service as it was at the time of backup. |  [optional] |
|**encryptionDetails** | [**EncryptionDetails**](EncryptionDetails.md) |  |  [optional] |
|**originalStorageAccountOption** | **Boolean** | Original Storage Account Option |  [optional] |
|**recoveryPointId** | **String** | ID of the backup copy to be recovered. |  [optional] |
|**recoveryType** | [**RecoveryTypeEnum**](#RecoveryTypeEnum) | Type of this recovery. |  [optional] |
|**region** | **String** | Region in which the virtual machine is restored. |  [optional] |
|**restoreDiskLunList** | **List&lt;Integer&gt;** | List of Disk LUNs for partial restore |  [optional] |
|**sourceResourceId** | **String** | Fully qualified ARM ID of the VM which is being recovered. |  [optional] |
|**storageAccountId** | **String** | Fully qualified ARM ID of the storage account to which the VM has to be restored. |  [optional] |
|**subnetId** | **String** | Subnet ID, is the subnet ID associated with the to be restored VM. For Classic VMs it would be  {VnetID}/Subnet/{SubnetName} and, for the Azure Resource Manager VMs it would be ARM resource ID used to represent  the subnet. |  [optional] |
|**targetDomainNameId** | **String** | Fully qualified ARM ID of the domain name to be associated to the VM being restored. This applies only to Classic  Virtual Machines. |  [optional] |
|**targetResourceGroupId** | **String** | This is the ARM Id of the resource group that you want to create for this Virtual machine and other artifacts.  For e.g. /subscriptions/{subId}/resourcegroups/{rg} |  [optional] |
|**targetVirtualMachineId** | **String** | This is the complete ARM Id of the VM that will be created.  For e.g. /subscriptions/{subId}/resourcegroups/{rg}/provider/Microsoft.Compute/virtualmachines/{vm} |  [optional] |
|**virtualNetworkId** | **String** | This is the virtual network Id of the vnet that will be attached to the virtual machine.  User will be validated for join action permissions in the linked access. |  [optional] |



## Enum: RecoveryTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ORIGINAL_LOCATION | &quot;OriginalLocation&quot; |
| ALTERNATE_LOCATION | &quot;AlternateLocation&quot; |
| RESTORE_DISKS | &quot;RestoreDisks&quot; |
| OFFLINE | &quot;Offline&quot; |



