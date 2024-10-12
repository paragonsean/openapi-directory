

# ChannelConfigWithInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automod** | [**AutomodEnum**](#AutomodEnum) |  |  |
|**automodBehavior** | [**AutomodBehaviorEnum**](#AutomodBehaviorEnum) |  |  |
|**automodThresholds** | [**Thresholds**](Thresholds.md) |  |  [optional] |
|**blocklist** | **String** |  |  [optional] |
|**blocklistBehavior** | [**BlocklistBehaviorEnum**](#BlocklistBehaviorEnum) |  |  [optional] |
|**commands** | [**List&lt;Command&gt;**](Command.md) |  |  |
|**connectEvents** | **Boolean** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**customEvents** | **Boolean** |  |  |
|**grants** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**maxMessageLength** | **Integer** |  |  |
|**messageRetention** | **String** |  |  |
|**mutes** | **Boolean** |  |  |
|**name** | **String** |  |  |
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



