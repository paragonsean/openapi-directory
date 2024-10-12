

# ContainerServiceServicePrincipalProfile

Information about a service principal identity for the cluster to use for manipulating Azure APIs. Either secret or keyVaultSecretRef must be specified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | The ID for the service principal. |  |
|**keyVaultSecretRef** | [**KeyVaultSecretRef**](KeyVaultSecretRef.md) |  |  [optional] |
|**secret** | **String** | The secret password associated with the service principal in plain text. |  [optional] |



