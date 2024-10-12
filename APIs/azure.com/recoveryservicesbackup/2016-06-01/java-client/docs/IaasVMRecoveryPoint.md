

# IaasVMRecoveryPoint

Azure VM (also known as IaaS VM) workload-specific backup copy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isInstantILRSessionActive** | **Boolean** | Answer to the question - Is the session to recover items from this backup copy still active. |  [optional] |
|**isSourceVMEncrypted** | **Boolean** | Identifies whether the VM was encrypted when the backup copy is created. |  [optional] |
|**keyAndSecret** | [**KeyAndSecretDetails**](KeyAndSecretDetails.md) |  |  [optional] |
|**recoveryPointAdditionalInfo** | **String** | Additional information associated with this backup copy. |  [optional] |
|**recoveryPointTime** | **OffsetDateTime** | The date and time when the backup copy was created. |  [optional] |
|**recoveryPointType** | **String** | Type of the backup copy. |  [optional] |
|**sourceVMStorageType** | **String** | The storage type for the VM whose backup copy was created. |  [optional] |



