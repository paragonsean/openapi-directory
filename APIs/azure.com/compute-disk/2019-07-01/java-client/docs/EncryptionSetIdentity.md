

# EncryptionSetIdentity

The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | The object id of the Managed Identity Resource. This will be sent to the RP from ARM via the x-ms-identity-principal-id header in the PUT request if the resource has a systemAssigned(implicit) identity |  [optional] [readonly] |
|**tenantId** | **String** | The tenant id of the Managed Identity Resource. This will be sent to the RP from ARM via the x-ms-client-tenant-id header in the PUT request if the resource has a systemAssigned(implicit) identity |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of Managed Identity used by the DiskEncryptionSet. Only SystemAssigned is supported. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |



