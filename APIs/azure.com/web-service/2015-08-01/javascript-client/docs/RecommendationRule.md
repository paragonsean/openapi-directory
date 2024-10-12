# WebSiteManagementClient.RecommendationRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionName** | **String** | Name of action that is recommended by this rule in string | [optional] 
**channels** | **String** | List of available channels that this rule applies. | 
**description** | **String** | Localized detailed description of the rule | [optional] 
**displayName** | **String** | UI friendly name of the rule | [optional] 
**enabled** | **Number** | On/off flag indicating the rule is currently enabled or disabled. | [optional] 
**level** | **String** | Level of impact indicating how critical this rule is. | 
**message** | **String** | Localized name of the rule (Good for UI) | [optional] 
**name** | **String** | Unique name of the rule | [optional] 
**recommendationId** | **String** | Recommendation ID of an associated recommendation object tied to the rule, if exists.              If such an object doesn&#39;t exist, it is set to null. | [optional] 
**tags** | **[String]** | An array of category tags that the rule contains. | [optional] 



## Enum: ChannelsEnum


* `Notification` (value: `"Notification"`)

* `Api` (value: `"Api"`)

* `Email` (value: `"Email"`)

* `All` (value: `"All"`)





## Enum: LevelEnum


* `Critical` (value: `"Critical"`)

* `Warning` (value: `"Warning"`)

* `Information` (value: `"Information"`)

* `NonUrgentSuggestion` (value: `"NonUrgentSuggestion"`)




