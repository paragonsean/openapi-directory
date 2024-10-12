

# IaasVMILRRegistrationRequest

Restore files/folders from a backup copy of IaaS VM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**initiatorName** | **String** | iSCSI initiator name. |  [optional] |
|**recoveryPointId** | **String** | ID of the IaaS VM backup copy from where the files/folders have to be restored. |  [optional] |
|**renewExistingRegistration** | **Boolean** | Whether to renew existing registration with the iSCSI server. |  [optional] |
|**virtualMachineId** | **String** | Fully qualified ARM ID of the virtual machine whose the files / folders have to be restored. |  [optional] |



