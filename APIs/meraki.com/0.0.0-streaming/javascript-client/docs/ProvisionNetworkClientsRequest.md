# MerakiDashboardApi.ProvisionNetworkClientsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devicePolicy** | **String** | The policy to apply to the specified client. Can be &#39;Group policy&#39;, &#39;Whitelisted&#39;, &#39;Allowed&#39;, &#39;Blocked&#39;, &#39;Per connection&#39; or &#39;Normal&#39;. Required. | 
**groupPolicyId** | **String** | The ID of the desired group policy to apply to the client. Required if &#39;devicePolicy&#39; is set to \&quot;Group policy\&quot;. Otherwise this is ignored. | [optional] 
**mac** | **String** | The MAC address of the client. Required. | 
**name** | **String** | The display name for the client. Optional. Limited to 255 bytes. | [optional] 
**policiesBySecurityAppliance** | [**ProvisionNetworkClientsRequestPoliciesBySecurityAppliance**](ProvisionNetworkClientsRequestPoliciesBySecurityAppliance.md) |  | [optional] 
**policiesBySsid** | [**ProvisionNetworkClientsRequestPoliciesBySsid**](ProvisionNetworkClientsRequestPoliciesBySsid.md) |  | [optional] 



## Enum: DevicePolicyEnum


* `Allowed` (value: `"Allowed"`)

* `Blocked` (value: `"Blocked"`)

* `Group policy` (value: `"Group policy"`)

* `Normal` (value: `"Normal"`)

* `Per connection` (value: `"Per connection"`)

* `Whitelisted` (value: `"Whitelisted"`)




