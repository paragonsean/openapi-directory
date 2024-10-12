

# IaasVMRecoveryPoint

IaaS VM workload specific backup copy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isInstantIlrSessionActive** | **Boolean** | Is the session to recover items from this backup copy still active. |  [optional] |
|**isManagedVirtualMachine** | **Boolean** | Whether VM is with Managed Disks |  [optional] |
|**isSourceVMEncrypted** | **Boolean** | Identifies whether the VM was encrypted when the backup copy is created. |  [optional] [readonly] |
|**keyAndSecret** | [**KeyAndSecretDetails**](KeyAndSecretDetails.md) |  |  [optional] |
|**originalStorageAccountOption** | **Boolean** | Original Storage Account Option |  [optional] |
|**osType** | **String** | OS type |  [optional] |
|**recoveryPointAdditionalInfo** | **String** | Additional information associated with this backup copy. |  [optional] [readonly] |
|**recoveryPointDiskConfiguration** | [**RecoveryPointDiskConfiguration**](RecoveryPointDiskConfiguration.md) |  |  [optional] |
|**recoveryPointTierDetails** | [**List&lt;RecoveryPointTierInformation&gt;**](RecoveryPointTierInformation.md) | Recovery point tier information. |  [optional] |
|**recoveryPointTime** | **OffsetDateTime** | Time at which this backup copy was created. |  [optional] [readonly] |
|**recoveryPointType** | **String** | Type of the backup copy. |  [optional] [readonly] |
|**sourceVMStorageType** | **String** | Storage type of the VM whose backup copy is created. |  [optional] [readonly] |
|**virtualMachineSize** | **String** | Virtual Machine Size |  [optional] |



