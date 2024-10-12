

# GroupMetadataInteractionsJoin

An action indicating that someone has joined the group. This data requires a bearer token with the `private` scope.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**added** | **Boolean** | Whether the authenticated user has followed this group. This data requires a bearer token with the &#x60;private&#x60; scope. |  |
|**addedTime** | **String** | The time in ISO 8601 format when the user joined this group. This data requires a bearer token with the &#x60;private&#x60; scope. |  |
|**title** | **String** | The user&#39;s title, or the null value if not applicable. This data requires a bearer token with the &#x60;private&#x60; scope. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Whether the authenticated user is a moderator or subscriber. This data requires a bearer token with the &#x60;private&#x60; scope.  Option descriptions:  * &#x60;member&#x60; - The authenticated user is a member.  * &#x60;moderator&#x60; - The authenticated user is a moderator.  |  |
|**uri** | **String** | The URI for following. PUT to this URI to follow, or DELETE to this URI to unfollow. This data requires a bearer token with the &#x60;private&#x60; scope. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MEMBER | &quot;member&quot; |
| MODERATOR | &quot;moderator&quot; |



