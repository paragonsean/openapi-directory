# MerakiDashboardApi.CreateNetworkGroupPolicyRequestBonjourForwarding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**[CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner]**](CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner.md) | A list of the Bonjour forwarding rules for your group policy. If &#39;settings&#39; is set to &#39;custom&#39;, at least one rule must be specified. | [optional] 
**settings** | **String** | How Bonjour rules are applied. Can be &#39;network default&#39;, &#39;ignore&#39; or &#39;custom&#39;. | [optional] 



## Enum: SettingsEnum


* `custom` (value: `"custom"`)

* `ignore` (value: `"ignore"`)

* `network default` (value: `"network default"`)




