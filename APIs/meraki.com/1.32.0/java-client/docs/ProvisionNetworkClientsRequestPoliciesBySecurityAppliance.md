

# ProvisionNetworkClientsRequestPoliciesBySecurityAppliance

An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**devicePolicy** | [**DevicePolicyEnum**](#DevicePolicyEnum) | The policy to apply to the specified client. Can be &#39;Allowed&#39;, &#39;Blocked&#39; or &#39;Normal&#39;. Required. |  [optional] |



## Enum: DevicePolicyEnum

| Name | Value |
|---- | -----|
| ALLOWED | &quot;Allowed&quot; |
| BLOCKED | &quot;Blocked&quot; |
| NORMAL | &quot;Normal&quot; |



