# StreamChatApi.UpdateChannelTypeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nameFromPath** | **String** |  | [optional] 
**automod** | **String** |  | 
**automodBehavior** | **String** |  | [optional] 
**automodThresholds** | [**ThresholdsRequest**](ThresholdsRequest.md) |  | [optional] 
**blocklist** | **String** |  | [optional] 
**blocklistBehavior** | **String** |  | [optional] 
**commands** | **[String]** | List of commands that channel supports | [optional] 
**connectEvents** | **Boolean** |  | [optional] 
**customEvents** | **Boolean** |  | [optional] 
**grants** | **{String: [String]}** |  | [optional] 
**maxMessageLength** | **Number** |  | [optional] 
**messageRetention** | **String** |  | [optional] 
**mutes** | **Boolean** |  | [optional] 
**permissions** | [**[PolicyRequest]**](PolicyRequest.md) |  | [optional] 
**pushNotifications** | **Boolean** |  | [optional] 
**quotes** | **Boolean** |  | [optional] 
**reactions** | **Boolean** |  | [optional] 
**readEvents** | **Boolean** |  | [optional] 
**reminders** | **Boolean** |  | [optional] 
**replies** | **Boolean** |  | [optional] 
**search** | **Boolean** |  | [optional] 
**typingEvents** | **Boolean** |  | [optional] 
**uploads** | **Boolean** |  | [optional] 
**urlEnrichment** | **Boolean** |  | [optional] 



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




