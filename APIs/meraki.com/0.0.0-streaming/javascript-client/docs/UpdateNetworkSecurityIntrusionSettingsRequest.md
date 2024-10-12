# MerakiDashboardApi.UpdateNetworkSecurityIntrusionSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idsRulesets** | **String** | Set the detection ruleset &#39;connectivity&#39;/&#39;balanced&#39;/&#39;security&#39; (optional - omitting will leave current config unchanged). Default value is &#39;balanced&#39; if none currently saved | [optional] 
**mode** | **String** | Set mode to &#39;disabled&#39;/&#39;detection&#39;/&#39;prevention&#39; (optional - omitting will leave current config unchanged) | [optional] 
**protectedNetworks** | [**UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks**](UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks.md) |  | [optional] 



## Enum: IdsRulesetsEnum


* `balanced` (value: `"balanced"`)

* `connectivity` (value: `"connectivity"`)

* `security` (value: `"security"`)





## Enum: ModeEnum


* `detection` (value: `"detection"`)

* `disabled` (value: `"disabled"`)

* `prevention` (value: `"prevention"`)




