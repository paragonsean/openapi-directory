

# UpdateNetworkSecurityIntrusionSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**idsRulesets** | [**IdsRulesetsEnum**](#IdsRulesetsEnum) | Set the detection ruleset &#39;connectivity&#39;/&#39;balanced&#39;/&#39;security&#39; (optional - omitting will leave current config unchanged). Default value is &#39;balanced&#39; if none currently saved |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Set mode to &#39;disabled&#39;/&#39;detection&#39;/&#39;prevention&#39; (optional - omitting will leave current config unchanged) |  [optional] |
|**protectedNetworks** | [**UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks**](UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks.md) |  |  [optional] |



## Enum: IdsRulesetsEnum

| Name | Value |
|---- | -----|
| BALANCED | &quot;balanced&quot; |
| CONNECTIVITY | &quot;connectivity&quot; |
| SECURITY | &quot;security&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| DETECTION | &quot;detection&quot; |
| DISABLED | &quot;disabled&quot; |
| PREVENTION | &quot;prevention&quot; |



