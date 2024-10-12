

# AccessPolicyEntry

An identity that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationId** | **UUID** |  Application ID of the client making request on behalf of a principal |  [optional] |
|**objectId** | **String** | The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies. |  |
|**permissions** | [**Permissions**](Permissions.md) |  |  |
|**tenantId** | **UUID** | The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. |  |



