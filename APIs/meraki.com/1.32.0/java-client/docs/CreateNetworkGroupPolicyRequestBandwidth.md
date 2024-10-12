

# CreateNetworkGroupPolicyRequestBandwidth

    The bandwidth settings for clients bound to your group policy. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidthLimits** | [**CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits**](CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits.md) |  |  [optional] |
|**settings** | [**SettingsEnum**](#SettingsEnum) | How bandwidth limits are enforced. Can be &#39;network default&#39;, &#39;ignore&#39; or &#39;custom&#39;. |  [optional] |



## Enum: SettingsEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;custom&quot; |
| IGNORE | &quot;ignore&quot; |
| NETWORK_DEFAULT | &quot;network default&quot; |



