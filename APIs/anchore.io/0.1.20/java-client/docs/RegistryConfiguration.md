

# RegistryConfiguration

A registry entry describing the endpoint and credentials for a registry to pull images from

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**lastUpated** | **OffsetDateTime** |  |  [optional] |
|**registry** | **String** | hostname:port string for accessing the registry, as would be used in a docker pull operation |  [optional] |
|**registryName** | **String** | human readable name associated with registry record |  [optional] |
|**registryType** | **String** | Type of registry |  [optional] |
|**registryUser** | **String** | Username portion of credential to use for this registry |  [optional] |
|**registryVerify** | **Boolean** | Use TLS/SSL verification for the registry URL |  [optional] |
|**userId** | **String** | Engine user that owns this registry entry |  [optional] |



