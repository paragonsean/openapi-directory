# MerakiDashboardApi.CreateNetworkGroupPolicyRequestVlanTagging

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **String** | How VLAN tagging is applied. Can be &#39;network default&#39;, &#39;ignore&#39; or &#39;custom&#39;. | [optional] 
**vlanId** | **String** | The ID of the vlan you want to tag. This only applies if &#39;settings&#39; is set to &#39;custom&#39;. | [optional] 



## Enum: SettingsEnum


* `custom` (value: `"custom"`)

* `ignore` (value: `"ignore"`)

* `network default` (value: `"network default"`)




