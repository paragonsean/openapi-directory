

# CreateNetworkGroupPolicyRequestVlanTagging

The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**settings** | [**SettingsEnum**](#SettingsEnum) | How VLAN tagging is applied. Can be &#39;network default&#39;, &#39;ignore&#39; or &#39;custom&#39;. |  [optional] |
|**vlanId** | **String** | The ID of the vlan you want to tag. This only applies if &#39;settings&#39; is set to &#39;custom&#39;. |  [optional] |



## Enum: SettingsEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;custom&quot; |
| IGNORE | &quot;ignore&quot; |
| NETWORK_DEFAULT | &quot;network default&quot; |



