

# UserWithStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**autoPlayNextVideo** | **Boolean** | Automatically start playing the upcoming video after the currently playing video |  [optional] |
|**autoPlayNextVideoPlaylist** | **Boolean** | Automatically start playing the video on the playlist after the currently playing video |  [optional] |
|**autoPlayVideo** | **Boolean** | Automatically start playing the video on the watch page |  [optional] |
|**blocked** | **Boolean** |  |  [optional] |
|**blockedReason** | **String** |  |  [optional] |
|**createdAt** | **String** |  |  [optional] |
|**email** | **String** | The user email |  [optional] |
|**emailVerified** | **Boolean** | Has the user confirmed their email address? |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastLoginDate** | **OffsetDateTime** |  |  [optional] |
|**noAccountSetupWarningModal** | **Boolean** |  |  [optional] |
|**noInstanceConfigWarningModal** | **Boolean** |  |  [optional] |
|**noWelcomeModal** | **Boolean** |  |  [optional] |
|**nsfwPolicy** | **NSFWPolicy** |  |  [optional] |
|**p2pEnabled** | **Boolean** | Enable P2P in the player |  [optional] |
|**pluginAuth** | **String** | Auth plugin to use to authenticate the user |  [optional] |
|**role** | [**UserRole**](UserRole.md) |  |  [optional] |
|**theme** | **String** | Theme enabled by this user |  [optional] |
|**username** | **String** | immutable name of the user, used to find or mention its actor |  [optional] |
|**videoChannels** | [**List&lt;VideoChannel&gt;**](VideoChannel.md) |  |  [optional] |
|**videoQuota** | **Integer** | The user video quota in bytes |  [optional] |
|**videoQuotaDaily** | **Integer** | The user daily video quota in bytes |  [optional] |
|**abusesAcceptedCount** | **Integer** | Count of reports/abuses created by the user and accepted/acted upon by the moderation team |  [optional] |
|**abusesCount** | **Integer** | Count of reports/abuses of which the user is a target |  [optional] |
|**abusesCreatedCount** | **Integer** | Count of reports/abuses created by the user |  [optional] |
|**videoCommentsCount** | **Integer** | Count of comments published |  [optional] |
|**videosCount** | **Integer** | Count of videos published |  [optional] |



