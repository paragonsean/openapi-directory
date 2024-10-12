# YouTubeDataApiV3.LiveChatBanSnippet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banDurationSeconds** | **String** | The duration of a ban, only filled if the ban has type TEMPORARY. | [optional] 
**bannedUserDetails** | [**ChannelProfileDetails**](ChannelProfileDetails.md) |  | [optional] 
**liveChatId** | **String** | The chat this ban is pertinent to. | [optional] 
**type** | **String** | The type of ban. | [optional] 



## Enum: TypeEnum


* `liveChatBanTypeUnspecified` (value: `"liveChatBanTypeUnspecified"`)

* `permanent` (value: `"permanent"`)

* `temporary` (value: `"temporary"`)




