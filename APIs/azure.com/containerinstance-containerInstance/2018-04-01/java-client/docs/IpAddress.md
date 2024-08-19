

# IpAddress

IP address for the container group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsNameLabel** | **String** | The Dns name label for the IP. |  [optional] |
|**fqdn** | **String** | The FQDN for the IP. |  [optional] [readonly] |
|**ip** | **String** | The IP exposed to the public internet. |  [optional] |
|**ports** | [**List&lt;Port&gt;**](Port.md) | The list of ports exposed on the container group. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Specifies if the IP is exposed to the public internet. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;Public&quot; |



