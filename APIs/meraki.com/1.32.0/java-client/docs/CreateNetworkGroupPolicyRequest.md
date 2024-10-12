

# CreateNetworkGroupPolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidth** | [**CreateNetworkGroupPolicyRequestBandwidth**](CreateNetworkGroupPolicyRequestBandwidth.md) |  |  [optional] |
|**bonjourForwarding** | [**CreateNetworkGroupPolicyRequestBonjourForwarding**](CreateNetworkGroupPolicyRequestBonjourForwarding.md) |  |  [optional] |
|**contentFiltering** | [**CreateNetworkGroupPolicyRequestContentFiltering**](CreateNetworkGroupPolicyRequestContentFiltering.md) |  |  [optional] |
|**firewallAndTrafficShaping** | [**CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping**](CreateNetworkGroupPolicyRequestFirewallAndTrafficShaping.md) |  |  [optional] |
|**name** | **String** | The name for your group policy. Required. |  |
|**scheduling** | [**CreateNetworkGroupPolicyRequestScheduling**](CreateNetworkGroupPolicyRequestScheduling.md) |  |  [optional] |
|**splashAuthSettings** | [**SplashAuthSettingsEnum**](#SplashAuthSettingsEnum) | Whether clients bound to your policy will bypass splash authorization or behave according to the network&#39;s rules. Can be one of &#39;network default&#39; or &#39;bypass&#39;. Only available if your network has a wireless configuration. |  [optional] |
|**vlanTagging** | [**CreateNetworkGroupPolicyRequestVlanTagging**](CreateNetworkGroupPolicyRequestVlanTagging.md) |  |  [optional] |



## Enum: SplashAuthSettingsEnum

| Name | Value |
|---- | -----|
| BYPASS | &quot;bypass&quot; |
| NETWORK_DEFAULT | &quot;network default&quot; |



