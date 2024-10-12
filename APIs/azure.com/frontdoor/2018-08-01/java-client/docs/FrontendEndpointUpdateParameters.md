

# FrontendEndpointUpdateParameters

Frontend endpoint used in routing rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostName** | **String** | The host name of the frontendEndpoint. Must be a domain name. |  [optional] |
|**sessionAffinityEnabledState** | [**SessionAffinityEnabledStateEnum**](#SessionAffinityEnabledStateEnum) | Whether to allow session affinity on this host. Valid options are &#39;Enabled&#39; or &#39;Disabled&#39; |  [optional] |
|**sessionAffinityTtlSeconds** | **Integer** | UNUSED. This field will be ignored. The TTL to use in seconds for session affinity, if applicable. |  [optional] |
|**webApplicationFirewallPolicyLink** | [**FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink**](FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink.md) |  |  [optional] |



## Enum: SessionAffinityEnabledStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



