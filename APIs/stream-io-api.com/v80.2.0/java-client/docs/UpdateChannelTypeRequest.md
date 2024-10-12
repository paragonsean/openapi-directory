

# UpdateChannelTypeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nameFromPath** | **String** |  |  [optional] |
|**automod** | [**AutomodEnum**](#AutomodEnum) |  |  |
|**automodBehavior** | [**AutomodBehaviorEnum**](#AutomodBehaviorEnum) |  |  [optional] |
|**automodThresholds** | [**ThresholdsRequest**](ThresholdsRequest.md) |  |  [optional] |
|**blocklist** | **String** |  |  [optional] |
|**blocklistBehavior** | [**BlocklistBehaviorEnum**](#BlocklistBehaviorEnum) |  |  [optional] |
|**commands** | **List&lt;String&gt;** | List of commands that channel supports |  [optional] |
|**connectEvents** | **Boolean** |  |  [optional] |
|**customEvents** | **Boolean** |  |  [optional] |
|**grants** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**maxMessageLength** | **Integer** |  |  [optional] |
|**messageRetention** | **String** |  |  [optional] |
|**mutes** | **Boolean** |  |  [optional] |
|**permissions** | [**List&lt;PolicyRequest&gt;**](PolicyRequest.md) |  |  [optional] |
|**pushNotifications** | **Boolean** |  |  [optional] |
|**quotes** | **Boolean** |  |  [optional] |
|**reactions** | **Boolean** |  |  [optional] |
|**readEvents** | **Boolean** |  |  [optional] |
|**reminders** | **Boolean** |  |  [optional] |
|**replies** | **Boolean** |  |  [optional] |
|**search** | **Boolean** |  |  [optional] |
|**typingEvents** | **Boolean** |  |  [optional] |
|**uploads** | **Boolean** |  |  [optional] |
|**urlEnrichment** | **Boolean** |  |  [optional] |



## Enum: AutomodEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;disabled&quot; |
| SIMPLE | &quot;simple&quot; |
| AI | &quot;AI&quot; |



## Enum: AutomodBehaviorEnum

| Name | Value |
|---- | -----|
| FLAG | &quot;flag&quot; |
| BLOCK | &quot;block&quot; |



## Enum: BlocklistBehaviorEnum

| Name | Value |
|---- | -----|
| FLAG | &quot;flag&quot; |
| BLOCK | &quot;block&quot; |



