

# RecommendationRule

Represents a recommendation rule that the recommendation engine can perform

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionName** | **String** | Name of action that is recommended by this rule in string |  [optional] |
|**channels** | [**ChannelsEnum**](#ChannelsEnum) | List of available channels that this rule applies. |  |
|**description** | **String** | Localized detailed description of the rule |  [optional] |
|**displayName** | **String** | UI friendly name of the rule |  [optional] |
|**enabled** | **Integer** | On/off flag indicating the rule is currently enabled or disabled. |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | Level of impact indicating how critical this rule is. |  |
|**message** | **String** | Localized name of the rule (Good for UI) |  [optional] |
|**name** | **String** | Unique name of the rule |  [optional] |
|**recommendationId** | **String** | Recommendation ID of an associated recommendation object tied to the rule, if exists.              If such an object doesn&#39;t exist, it is set to null. |  [optional] |
|**tags** | **List&lt;String&gt;** | An array of category tags that the rule contains. |  [optional] |



## Enum: ChannelsEnum

| Name | Value |
|---- | -----|
| NOTIFICATION | &quot;Notification&quot; |
| API | &quot;Api&quot; |
| EMAIL | &quot;Email&quot; |
| ALL | &quot;All&quot; |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| CRITICAL | &quot;Critical&quot; |
| WARNING | &quot;Warning&quot; |
| INFORMATION | &quot;Information&quot; |
| NON_URGENT_SUGGESTION | &quot;NonUrgentSuggestion&quot; |



