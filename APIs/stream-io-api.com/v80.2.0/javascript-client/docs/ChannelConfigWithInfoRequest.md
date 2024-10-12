# StreamChatApi.ChannelConfigWithInfoRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automod** | **String** |  | 
**automodBehavior** | **String** |  | [optional] 
**automodThresholds** | [**ThresholdsRequest**](ThresholdsRequest.md) |  | [optional] 
**blocklist** | **String** |  | [optional] 
**blocklistBehavior** | **String** |  | [optional] 
**commands** | [**[CommandRequest]**](CommandRequest.md) |  | [optional] 
**connectEvents** | **Boolean** |  | [optional] 
**createdAt** | **Date** |  | [optional] 
**customEvents** | **Boolean** |  | [optional] 
**grants** | **{String: [String]}** |  | [optional] 
**maxMessageLength** | **Number** |  | [optional] 
**messageRetention** | **String** |  | [optional] 
**mutes** | **Boolean** |  | [optional] 
**name** | **String** |  | [optional] 
**pushNotifications** | **Boolean** |  | [optional] 
**quotes** | **Boolean** |  | [optional] 
**reactions** | **Boolean** |  | [optional] 
**readEvents** | **Boolean** |  | [optional] 
**reminders** | **Boolean** |  | [optional] 
**replies** | **Boolean** |  | [optional] 
**search** | **Boolean** |  | [optional] 
**typingEvents** | **Boolean** |  | [optional] 
**updatedAt** | **Date** |  | [optional] 
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




