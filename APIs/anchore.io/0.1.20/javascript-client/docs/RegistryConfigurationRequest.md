# AnchoreEngineApiServer.RegistryConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry** | **String** | hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/_* or gcr.io/myproject/myrepository) | [optional] 
**registryName** | **String** | human readable name associated with registry record | [optional] 
**registryPass** | **String** | Password portion of credential to use for this registry | [optional] 
**registryType** | **String** | Type of registry | [optional] 
**registryUser** | **String** | Username portion of credential to use for this registry | [optional] 
**registryVerify** | **Boolean** | Use TLS/SSL verification for the registry URL | [optional] 


