# RecoveryServicesBackupClient.IaasVMRestoreRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityGroup** | **String** | The affinity group associated with the VM to be restored. Affinity groups are used only for Classic-deployed virtual machines. | [optional] 
**createNewCloudService** | **Boolean** | Asks the question if a new cloud service should be created while restoring the VM. If the answer is false, the VM is restored to the same cloud service. | [optional] 
**encryptionDetails** | [**EncryptionDetails**](EncryptionDetails.md) |  | [optional] 
**recoveryPointId** | **String** | The ID of the backup copy to be recovered. | [optional] 
**recoveryType** | **String** | The type of this recovery. | [optional] 
**region** | **String** | The region where the virtual machine is restored. | [optional] 
**sourceResourceId** | **String** | The fully qualified Resource Manager ID of the VM being recovered. | [optional] 
**storageAccountId** | **String** | The fully qualified Resource Manager ID of the storage account where the VM will be restored. | [optional] 
**subnetId** | **String** | Subnet ID is the identifier for the VM to be restored. For Classic VMs the subnet ID would be {VnetID}/Subnet/{SubnetName}, and for the Resource Manager VMs, the subnet ID would be the Resource Manager resource ID used to represent the subnet. | [optional] 
**targetDomainNameId** | **String** | The fully qualified Resource Manager ID of the domain name to be associated with the VM being restored. Use the Resource Manager ID to identify the domain, only for Classic-deployed virtual machines. | [optional] 
**targetResourceGroupId** | **String** | The Resource Manager ID of the resource group you&#39;re creating for this VM and other artifacts.      For example: /subscriptions/{subId}/resourcegroups/{rg} | [optional] 
**targetVirtualMachineId** | **String** | The complete Resource Manager ID of the VM that will be created.              For example: /subscriptions/{subId}/resourcegroups/{rg}/provider/Microsoft.Compute/virtualmachines/{vm} | [optional] 
**virtualNetworkId** | **String** | This is the virtual network ID of the vnet that is attached to the virtual machine.              Your join action permissions are validated during the linked access. | [optional] 



## Enum: RecoveryTypeEnum


* `Invalid` (value: `"Invalid"`)

* `OriginalLocation` (value: `"OriginalLocation"`)

* `AlternateLocation` (value: `"AlternateLocation"`)

* `RestoreDisks` (value: `"RestoreDisks"`)




