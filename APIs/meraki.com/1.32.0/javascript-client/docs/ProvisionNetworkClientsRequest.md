# MerakiDashboardApi.ProvisionNetworkClientsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**[ProvisionNetworkClientsRequestClientsInner]**](ProvisionNetworkClientsRequestClientsInner.md) | The array of clients to provision | 
**devicePolicy** | **String** | The policy to apply to the specified client. Can be &#39;Group policy&#39;, &#39;Allowed&#39;, &#39;Blocked&#39;, &#39;Per connection&#39; or &#39;Normal&#39;. Required. | 
**groupPolicyId** | **String** | The ID of the desired group policy to apply to the client. Required if &#39;devicePolicy&#39; is set to \&quot;Group policy\&quot;. Otherwise this is ignored. | [optional] 
**policiesBySecurityAppliance** | [**ProvisionNetworkClientsRequestPoliciesBySecurityAppliance**](ProvisionNetworkClientsRequestPoliciesBySecurityAppliance.md) |  | [optional] 
**policiesBySsid** | [**ProvisionNetworkClientsRequestPoliciesBySsid**](ProvisionNetworkClientsRequestPoliciesBySsid.md) |  | [optional] 



## Enum: DevicePolicyEnum


* `Allowed` (value: `"Allowed"`)

* `Blocked` (value: `"Blocked"`)

* `Group policy` (value: `"Group policy"`)

* `Normal` (value: `"Normal"`)

* `Per connection` (value: `"Per connection"`)




