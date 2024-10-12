

# GroupUsersListByGroups200ResponseValueInner

User profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Email address. |  [optional] |
|**firstName** | **String** | First name. |  [optional] |
|**id** | **String** | User identifier path. |  [optional] |
|**identities** | [**List&lt;GroupUsersListByGroups200ResponseValueInnerIdentitiesInner&gt;**](GroupUsersListByGroups200ResponseValueInnerIdentitiesInner.md) | Collection of user identities. |  [optional] [readonly] |
|**lastName** | **String** | Last name. |  [optional] |
|**note** | **String** | Administrator&#39;s note about given user. |  [optional] |
|**registrationDate** | **OffsetDateTime** | Date of user registration. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | User state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| BLOCKED | &quot;Blocked&quot; |



