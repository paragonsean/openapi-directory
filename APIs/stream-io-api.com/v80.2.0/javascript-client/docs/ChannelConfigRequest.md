# StreamChatApi.ChannelConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocklist** | **String** |  | [optional] 
**blocklistBehavior** | **String** |  | [optional] 
**commands** | **[String]** |  | [optional] 
**grants** | **{String: [String]}** |  | [optional] 
**maxMessageLength** | **Number** | Overrides max message length | [optional] 
**quotes** | **Boolean** | Enables message quotes | [optional] 
**reactions** | **Boolean** | Enables or disables reactions | [optional] 
**replies** | **Boolean** | Enables message replies (threads) | [optional] 
**typingEvents** | **Boolean** | Enables or disables typing events | [optional] 
**uploads** | **Boolean** | Enables or disables file uploads | [optional] 
**urlEnrichment** | **Boolean** | Enables or disables URL enrichment | [optional] 



## Enum: BlocklistBehaviorEnum


* `flag` (value: `"flag"`)

* `block` (value: `"block"`)




