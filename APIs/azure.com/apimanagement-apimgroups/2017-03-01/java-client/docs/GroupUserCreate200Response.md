

# GroupUserCreate200Response

User details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Identifier of the entity. |  [optional] |
|**email** | **String** | Email address. |  [optional] |
|**firstName** | **String** | First name. |  [optional] |
|**groups** | [**List&lt;GroupUserCreate200ResponseAllOfGroupsInner&gt;**](GroupUserCreate200ResponseAllOfGroupsInner.md) | Collection of groups user is part of. |  [optional] [readonly] |
|**lastName** | **String** | Last name. |  [optional] |
|**registrationDate** | **OffsetDateTime** | Date of user registration. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |
|**identities** | [**List&lt;GroupUserCreate200ResponseAllOfAllOfIdentitiesInner&gt;**](GroupUserCreate200ResponseAllOfAllOfIdentitiesInner.md) | Collection of user identities. |  [optional] [readonly] |
|**note** | **String** | Optional note about a user set by the administrator. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| BLOCKED | &quot;blocked&quot; |



