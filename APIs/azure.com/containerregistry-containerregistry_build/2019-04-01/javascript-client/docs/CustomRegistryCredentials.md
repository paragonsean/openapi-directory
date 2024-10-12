# ContainerRegistryManagementClient.CustomRegistryCredentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | **String** | Indicates the managed identity assigned to the custom credential. If a user-assigned identity  this value is the Client ID. If a system-assigned identity, the value will be &#x60;system&#x60;. In  the case of a system-assigned identity, the Client ID will be determined by the runner. This  identity may be used to authenticate to key vault to retrieve credentials or it may be the only   source of authentication used for accessing the registry. | [optional] 
**password** | [**SecretObject**](SecretObject.md) |  | [optional] 
**userName** | [**SecretObject**](SecretObject.md) |  | [optional] 


