# NetworkManagementClient.ConnectivityIssue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **[{String: String}]** | Provides additional context on the issue. | [optional] [readonly] 
**origin** | **String** | The origin of the issue. | [optional] [readonly] 
**severity** | **String** | The severity of the issue. | [optional] [readonly] 
**type** | **String** | The type of issue. | [optional] [readonly] 



## Enum: OriginEnum


* `Local` (value: `"Local"`)

* `Inbound` (value: `"Inbound"`)

* `Outbound` (value: `"Outbound"`)





## Enum: SeverityEnum


* `Error` (value: `"Error"`)

* `Warning` (value: `"Warning"`)





## Enum: TypeEnum


* `Unknown` (value: `"Unknown"`)

* `AgentStopped` (value: `"AgentStopped"`)

* `GuestFirewall` (value: `"GuestFirewall"`)

* `DnsResolution` (value: `"DnsResolution"`)

* `SocketBind` (value: `"SocketBind"`)

* `NetworkSecurityRule` (value: `"NetworkSecurityRule"`)

* `UserDefinedRoute` (value: `"UserDefinedRoute"`)

* `PortThrottled` (value: `"PortThrottled"`)

* `Platform` (value: `"Platform"`)




