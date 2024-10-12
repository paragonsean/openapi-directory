

# LiveChatBanSnippet


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**banDurationSeconds** | **String** | The duration of a ban, only filled if the ban has type TEMPORARY. |  [optional] |
|**bannedUserDetails** | [**ChannelProfileDetails**](ChannelProfileDetails.md) |  |  [optional] |
|**liveChatId** | **String** | The chat this ban is pertinent to. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of ban. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LIVE_CHAT_BAN_TYPE_UNSPECIFIED | &quot;liveChatBanTypeUnspecified&quot; |
| PERMANENT | &quot;permanent&quot; |
| TEMPORARY | &quot;temporary&quot; |



