

# ManagedClusterAADProfile

AADProfile specifies attributes for Azure Active Directory integration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientAppID** | **String** | The client AAD application ID. |  |
|**serverAppID** | **String** | The server AAD application ID. |  |
|**serverAppSecret** | **String** | The server AAD application secret. |  [optional] |
|**tenantID** | **String** | The AAD tenant ID to use for authentication. If not specified, will use the tenant of the deployment subscription. |  [optional] |



