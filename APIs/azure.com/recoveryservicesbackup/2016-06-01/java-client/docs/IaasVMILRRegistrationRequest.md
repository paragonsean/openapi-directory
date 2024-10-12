

# IaasVMILRRegistrationRequest

Restore files or folders from a backup copy, or recovery point, of an IaaS (or Azure) VM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**initiatorName** | **String** | The iSCSI initiator name. |  [optional] |
|**recoveryPointId** | **String** | The ID of the IaaS VM recovery point used to restore the files or folders. |  [optional] |
|**renewExistingRegistration** | **Boolean** | Whether to renew the existing registration with the iSCSI server. |  [optional] |
|**virtualMachineId** | **String** | The fully qualified Resource Manager ID of the VM used to restore the files or folders. |  [optional] |



