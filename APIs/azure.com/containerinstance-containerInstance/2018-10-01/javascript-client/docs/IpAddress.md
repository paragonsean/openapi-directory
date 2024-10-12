# ContainerInstanceManagementClient.IpAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsNameLabel** | **String** | The Dns name label for the IP. | [optional] 
**fqdn** | **String** | The FQDN for the IP. | [optional] [readonly] 
**ip** | **String** | The IP exposed to the public internet. | [optional] 
**ports** | [**[Port]**](Port.md) | The list of ports exposed on the container group. | 
**type** | **String** | Specifies if the IP is exposed to the public internet or private VNET. | 



## Enum: TypeEnum


* `Public` (value: `"Public"`)

* `Private` (value: `"Private"`)




