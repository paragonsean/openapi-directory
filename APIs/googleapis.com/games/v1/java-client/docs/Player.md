

# Player

A Player resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avatarImageUrl** | **String** | The base URL for the image that represents the player. |  [optional] |
|**bannerUrlLandscape** | **String** | The url to the landscape mode player banner image. |  [optional] |
|**bannerUrlPortrait** | **String** | The url to the portrait mode player banner image. |  [optional] |
|**displayName** | **String** | The name to display for the player. |  [optional] |
|**experienceInfo** | [**PlayerExperienceInfo**](PlayerExperienceInfo.md) |  |  [optional] |
|**friendStatus** | [**FriendStatusEnum**](#FriendStatusEnum) | The friend status of the given player, relative to the requester. This is unset if the player is not sharing their friends list with the game. |  [optional] |
|**gamePlayerId** | **String** | Per-application unique player identifier. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#player&#x60; |  [optional] |
|**name** | [**PlayerName**](PlayerName.md) |  |  [optional] |
|**originalPlayerId** | **String** | The player ID that was used for this player the first time they signed into the game in question. This is only populated for calls to player.get for the requesting player, only if the player ID has subsequently changed, and only to clients that support remapping player IDs. |  [optional] |
|**playerId** | **String** | The ID of the player. |  [optional] |
|**profileSettings** | [**ProfileSettings**](ProfileSettings.md) |  |  [optional] |
|**title** | **String** | The player&#39;s title rewarded for their game activities. |  [optional] |



## Enum: FriendStatusEnum

| Name | Value |
|---- | -----|
| NO_RELATIONSHIP | &quot;NO_RELATIONSHIP&quot; |
| FRIEND | &quot;FRIEND&quot; |



