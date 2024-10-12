# SecurityCenter.JitNetworkAccessPortRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedSourceAddressPrefix** | **String** | Mutually exclusive with the \&quot;allowedSourceAddressPrefixes\&quot; parameter. Should be an IP address or CIDR, for example \&quot;192.168.0.3\&quot; or \&quot;192.168.0.0/16\&quot;. | [optional] 
**allowedSourceAddressPrefixes** | **[String]** | Mutually exclusive with the \&quot;allowedSourceAddressPrefix\&quot; parameter. | [optional] 
**maxRequestAccessDuration** | **String** | Maximum duration requests can be made for. In ISO 8601 duration format. Minimum 5 minutes, maximum 1 day | 
**number** | **Number** |  | 
**protocol** | **String** |  | 



## Enum: ProtocolEnum


* `TCP` (value: `"TCP"`)

* `UDP` (value: `"UDP"`)

* `STAR` (value: `"*"`)




