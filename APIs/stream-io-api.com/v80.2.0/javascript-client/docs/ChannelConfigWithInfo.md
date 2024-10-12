# StreamChatApi.ChannelConfigWithInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automod** | **String** |  | 
**automodBehavior** | **String** |  | 
**automodThresholds** | [**Thresholds**](Thresholds.md) |  | [optional] 
**blocklist** | **String** |  | [optional] 
**blocklistBehavior** | **String** |  | [optional] 
**commands** | [**[Command]**](Command.md) |  | 
**connectEvents** | **Boolean** |  | 
**createdAt** | **Date** |  | 
**customEvents** | **Boolean** |  | 
**grants** | **{String: [String]}** |  | [optional] 
**maxMessageLength** | **Number** |  | 
**messageRetention** | **String** |  | 
**mutes** | **Boolean** |  | 
**name** | **String** |  | 
**pushNotifications** | **Boolean** |  | 
**quotes** | **Boolean** |  | 
**reactions** | **Boolean** |  | 
**readEvents** | **Boolean** |  | 
**reminders** | **Boolean** |  | 
**replies** | **Boolean** |  | 
**search** | **Boolean** |  | 
**typingEvents** | **Boolean** |  | 
**updatedAt** | **Date** |  | 
**uploads** | **Boolean** |  | 
**urlEnrichment** | **Boolean** |  | 



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




