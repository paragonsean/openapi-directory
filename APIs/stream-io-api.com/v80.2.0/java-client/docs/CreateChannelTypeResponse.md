

# CreateChannelTypeResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automod** | [**AutomodEnum**](#AutomodEnum) |  |  |
|**automodBehavior** | [**AutomodBehaviorEnum**](#AutomodBehaviorEnum) |  |  |
|**automodThresholds** | [**Thresholds**](Thresholds.md) |  |  [optional] |
|**blocklist** | **String** |  |  [optional] |
|**blocklistBehavior** | [**BlocklistBehaviorEnum**](#BlocklistBehaviorEnum) |  |  [optional] |
|**commands** | **List&lt;String&gt;** |  |  |
|**connectEvents** | **Boolean** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**customEvents** | **Boolean** |  |  |
|**duration** | **String** |  |  |
|**grants** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  |
|**maxMessageLength** | **Integer** |  |  |
|**messageRetention** | **String** |  |  |
|**mutes** | **Boolean** |  |  |
|**name** | **String** |  |  |
|**permissions** | [**List&lt;PolicyRequest1&gt;**](PolicyRequest1.md) |  |  |
|**pushNotifications** | **Boolean** |  |  |
|**quotes** | **Boolean** |  |  |
|**reactions** | **Boolean** |  |  |
|**readEvents** | **Boolean** |  |  |
|**reminders** | **Boolean** |  |  |
|**replies** | **Boolean** |  |  |
|**search** | **Boolean** |  |  |
|**typingEvents** | **Boolean** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**uploads** | **Boolean** |  |  |
|**urlEnrichment** | **Boolean** |  |  |



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



