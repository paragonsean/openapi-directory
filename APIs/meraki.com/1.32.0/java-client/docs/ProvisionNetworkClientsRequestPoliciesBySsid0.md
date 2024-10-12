

# ProvisionNetworkClientsRequestPoliciesBySsid0

The number for the SSID

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**devicePolicy** | [**DevicePolicyEnum**](#DevicePolicyEnum) | The policy to apply to the specified client. Can be &#39;Allowed&#39;, &#39;Blocked&#39;, &#39;Normal&#39; or &#39;Group policy&#39;. Required. |  |
|**groupPolicyId** | **String** | The ID of the desired group policy to apply to the client. Required if &#39;devicePolicy&#39; is set to \&quot;Group policy\&quot;. Otherwise this is ignored. |  [optional] |



## Enum: DevicePolicyEnum

| Name | Value |
|---- | -----|
| ALLOWED | &quot;Allowed&quot; |
| BLOCKED | &quot;Blocked&quot; |
| GROUP_POLICY | &quot;Group policy&quot; |
| NORMAL | &quot;Normal&quot; |



