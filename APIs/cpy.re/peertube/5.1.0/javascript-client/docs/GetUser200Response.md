# PeerTube.GetUser200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Account**](Account.md) |  | [optional] 
**autoPlayNextVideo** | **Boolean** | Automatically start playing the upcoming video after the currently playing video | [optional] 
**autoPlayNextVideoPlaylist** | **Boolean** | Automatically start playing the video on the playlist after the currently playing video | [optional] 
**autoPlayVideo** | **Boolean** | Automatically start playing the video on the watch page | [optional] 
**blocked** | **Boolean** |  | [optional] 
**blockedReason** | **String** |  | [optional] 
**createdAt** | **String** |  | [optional] 
**email** | **String** | The user email | [optional] 
**emailVerified** | **Boolean** | Has the user confirmed their email address? | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastLoginDate** | **Date** |  | [optional] 
**noAccountSetupWarningModal** | **Boolean** |  | [optional] 
**noInstanceConfigWarningModal** | **Boolean** |  | [optional] 
**noWelcomeModal** | **Boolean** |  | [optional] 
**nsfwPolicy** | [**NSFWPolicy**](NSFWPolicy.md) |  | [optional] 
**p2pEnabled** | **Boolean** | Enable P2P in the player | [optional] 
**pluginAuth** | **String** | Auth plugin to use to authenticate the user | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**theme** | **String** | Theme enabled by this user | [optional] 
**username** | **String** | immutable name of the user, used to find or mention its actor | [optional] 
**videoChannels** | [**[VideoChannel]**](VideoChannel.md) |  | [optional] 
**videoQuota** | **Number** | The user video quota in bytes | [optional] 
**videoQuotaDaily** | **Number** | The user daily video quota in bytes | [optional] 
**abusesAcceptedCount** | **Number** | Count of reports/abuses created by the user and accepted/acted upon by the moderation team | [optional] 
**abusesCount** | **Number** | Count of reports/abuses of which the user is a target | [optional] 
**abusesCreatedCount** | **Number** | Count of reports/abuses created by the user | [optional] 
**videoCommentsCount** | **Number** | Count of comments published | [optional] 
**videosCount** | **Number** | Count of videos published | [optional] 


