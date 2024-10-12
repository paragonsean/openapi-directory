# Vimeo.ChannelMetadataInteractionsFollow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | **Boolean** | Whether the authenticated user has followed this channel. This data requires a bearer token with the &#x60;private&#x60; scope. | 
**addedTime** | **String** | The time in ISO 8601 format that the user followed this channel, or the null value if the user hasn&#39;t followed the channel. This data requires a bearer token with the &#x60;private&#x60; scope. | 
**type** | **String** | Whether the authenticated user is a moderator or subscriber. This data requires a bearer token with the &#x60;private&#x60; scope.  Option descriptions:  * &#x60;moderator&#x60; - The authenticated user is a moderator.  * &#x60;subscriber&#x60; - The authenticated user is a subscriber.  | 
**uri** | **String** | The URI for following or unfollowing this channel. PUT to this URI to follow the channel, or DELETE to this URI to unfollow the channel. This data requires a bearer token with the &#x60;private&#x60; scope. | 



## Enum: TypeEnum


* `moderator` (value: `"moderator"`)

* `subscriber` (value: `"subscriber"`)




