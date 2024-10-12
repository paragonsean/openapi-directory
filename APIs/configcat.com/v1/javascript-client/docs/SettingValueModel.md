# ConfigCatPublicManagementApi.SettingValueModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**ConfigModel**](ConfigModel.md) |  | [optional] 
**environment** | [**EnvironmentModel**](EnvironmentModel.md) |  | [optional] 
**integrationLinks** | [**[IntegrationLinkModel]**](IntegrationLinkModel.md) |  | [optional] 
**lastUpdaterUserEmail** | **String** |  | [optional] 
**lastUpdaterUserFullName** | **String** |  | [optional] 
**readOnly** | **Boolean** |  | [optional] 
**rolloutPercentageItems** | [**[RolloutPercentageItemModel]**](RolloutPercentageItemModel.md) | The percentage rule collection. | [optional] 
**rolloutRules** | [**[RolloutRuleModel]**](RolloutRuleModel.md) | The targeting rule collection. | [optional] 
**setting** | [**SettingDataModel**](SettingDataModel.md) |  | [optional] 
**settingTags** | [**[SettingTagModel]**](SettingTagModel.md) |  | [optional] 
**updatedAt** | **Date** |  | [optional] 
**value** | **Object** | The value to serve. It must respect the setting type. | [optional] 


