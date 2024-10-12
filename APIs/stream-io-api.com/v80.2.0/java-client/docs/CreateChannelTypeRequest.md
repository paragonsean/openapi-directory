

# CreateChannelTypeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automod** | [**AutomodEnum**](#AutomodEnum) | Enables automatic message moderation |  |
|**automodBehavior** | [**AutomodBehaviorEnum**](#AutomodBehaviorEnum) | Sets behavior of automatic moderation |  [optional] |
|**blocklist** | **String** | Name of the blocklist to use |  [optional] |
|**blocklistBehavior** | [**BlocklistBehaviorEnum**](#BlocklistBehaviorEnum) | Sets behavior of blocklist |  [optional] |
|**commands** | **List&lt;String&gt;** | List of commands that channel supports |  [optional] |
|**connectEvents** | **Boolean** | Connect events support |  [optional] |
|**customEvents** | **Boolean** | Enables custom events |  [optional] |
|**grants** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**maxMessageLength** | **Integer** | Number of maximum message characters |  [optional] |
|**messageRetention** | **String** | Number of days to keep messages. &#39;infinite&#39; disables retention |  [optional] |
|**mutes** | **Boolean** | Enables mutes |  [optional] |
|**name** | **String** | Channel type name |  |
|**permissions** | [**List&lt;PolicyRequest&gt;**](PolicyRequest.md) | List of permissions for the channel type |  [optional] |
|**pushNotifications** | **Boolean** | Enables push notifications |  [optional] |
|**reactions** | **Boolean** | Enables message reactions |  [optional] |
|**readEvents** | **Boolean** | Read events support |  [optional] |
|**replies** | **Boolean** | Enables message replies (threads) |  [optional] |
|**search** | **Boolean** | Enables message search |  [optional] |
|**typingEvents** | **Boolean** | Typing events support |  [optional] |
|**uploads** | **Boolean** | Enables file uploads |  [optional] |
|**urlEnrichment** | **Boolean** | Enables URL enrichment |  [optional] |



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



