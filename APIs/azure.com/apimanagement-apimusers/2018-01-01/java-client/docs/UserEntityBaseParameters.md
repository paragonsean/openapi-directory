

# UserEntityBaseParameters

User Entity Base Parameters set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identities** | [**List&lt;UserIdentityContract&gt;**](UserIdentityContract.md) | Collection of user identities. |  [optional] |
|**note** | **String** | Optional note about a user set by the administrator. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| BLOCKED | &quot;blocked&quot; |
| PENDING | &quot;pending&quot; |
| DELETED | &quot;deleted&quot; |



