

# LiveChatUserBannedMessageDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**banDurationSeconds** | **String** | The duration of the ban. This property is only present if the banType is temporary. |  [optional] |
|**banType** | [**BanTypeEnum**](#BanTypeEnum) | The type of ban. |  [optional] |
|**bannedUserDetails** | [**ChannelProfileDetails**](ChannelProfileDetails.md) |  |  [optional] |



## Enum: BanTypeEnum

| Name | Value |
|---- | -----|
| PERMANENT | &quot;permanent&quot; |
| TEMPORARY | &quot;temporary&quot; |



