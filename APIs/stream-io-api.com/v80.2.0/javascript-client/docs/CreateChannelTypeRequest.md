# StreamChatApi.CreateChannelTypeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automod** | **String** | Enables automatic message moderation | 
**automodBehavior** | **String** | Sets behavior of automatic moderation | [optional] 
**blocklist** | **String** | Name of the blocklist to use | [optional] 
**blocklistBehavior** | **String** | Sets behavior of blocklist | [optional] 
**commands** | **[String]** | List of commands that channel supports | [optional] 
**connectEvents** | **Boolean** | Connect events support | [optional] 
**customEvents** | **Boolean** | Enables custom events | [optional] 
**grants** | **{String: [String]}** |  | [optional] 
**maxMessageLength** | **Number** | Number of maximum message characters | [optional] 
**messageRetention** | **String** | Number of days to keep messages. &#39;infinite&#39; disables retention | [optional] 
**mutes** | **Boolean** | Enables mutes | [optional] 
**name** | **String** | Channel type name | 
**permissions** | [**[PolicyRequest]**](PolicyRequest.md) | List of permissions for the channel type | [optional] 
**pushNotifications** | **Boolean** | Enables push notifications | [optional] 
**reactions** | **Boolean** | Enables message reactions | [optional] 
**readEvents** | **Boolean** | Read events support | [optional] 
**replies** | **Boolean** | Enables message replies (threads) | [optional] 
**search** | **Boolean** | Enables message search | [optional] 
**typingEvents** | **Boolean** | Typing events support | [optional] 
**uploads** | **Boolean** | Enables file uploads | [optional] 
**urlEnrichment** | **Boolean** | Enables URL enrichment | [optional] 



## Enum: AutomodEnum


* `disabled` (value: `"disabled"`)

* `simple` (value: `"simple"`)

* `AI` (value: `"AI"`)





## Enum: AutomodBehaviorEnum


* `flag` (value: `"flag"`)

* `block` (value: `"block"`)





## Enum: BlocklistBehaviorEnum


* `flag` (value: `"flag"`)

* `block` (value: `"block"`)




