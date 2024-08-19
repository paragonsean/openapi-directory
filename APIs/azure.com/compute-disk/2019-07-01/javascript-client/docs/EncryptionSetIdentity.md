# DiskResourceProviderClient.EncryptionSetIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | The object id of the Managed Identity Resource. This will be sent to the RP from ARM via the x-ms-identity-principal-id header in the PUT request if the resource has a systemAssigned(implicit) identity | [optional] [readonly] 
**tenantId** | **String** | The tenant id of the Managed Identity Resource. This will be sent to the RP from ARM via the x-ms-client-tenant-id header in the PUT request if the resource has a systemAssigned(implicit) identity | [optional] [readonly] 
**type** | **String** | The type of Managed Identity used by the DiskEncryptionSet. Only SystemAssigned is supported. | [optional] 



## Enum: TypeEnum


* `SystemAssigned` (value: `"SystemAssigned"`)




