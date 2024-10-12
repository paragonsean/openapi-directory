

# ChannelConfigRequest

Channel configuration overrides

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blocklist** | **String** |  |  [optional] |
|**blocklistBehavior** | [**BlocklistBehaviorEnum**](#BlocklistBehaviorEnum) |  |  [optional] |
|**commands** | **List&lt;String&gt;** |  |  [optional] |
|**grants** | **Map&lt;String, List&lt;String&gt;&gt;** |  |  [optional] |
|**maxMessageLength** | **Integer** | Overrides max message length |  [optional] |
|**quotes** | **Boolean** | Enables message quotes |  [optional] |
|**reactions** | **Boolean** | Enables or disables reactions |  [optional] |
|**replies** | **Boolean** | Enables message replies (threads) |  [optional] |
|**typingEvents** | **Boolean** | Enables or disables typing events |  [optional] |
|**uploads** | **Boolean** | Enables or disables file uploads |  [optional] |
|**urlEnrichment** | **Boolean** | Enables or disables URL enrichment |  [optional] |



## Enum: BlocklistBehaviorEnum

| Name | Value |
|---- | -----|
| FLAG | &quot;flag&quot; |
| BLOCK | &quot;block&quot; |



