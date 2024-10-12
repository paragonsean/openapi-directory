

# Credentials

The parameters that describes a set of credentials that will be used when a run is invoked.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customRegistries** | [**Map&lt;String, CustomRegistryCredentials&gt;**](CustomRegistryCredentials.md) | Describes the credential parameters for accessing other custom registries. The key  for the dictionary item will be the registry login server (myregistry.azurecr.io) and  the value of the item will be the registry credentials for accessing the registry. |  [optional] |
|**sourceRegistry** | [**SourceRegistryCredentials**](SourceRegistryCredentials.md) |  |  [optional] |



