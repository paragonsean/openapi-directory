

# UserBasics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstname** | **String** | Firstname of the user (for education users) |  [optional] |
|**id** | **String** | The user unique identifier |  [optional] |
|**isFlatTeam** | **Boolean** | Will be &#39;true&#39; if user is part of the Flat Team |  [optional] |
|**isPowerUser** | **Boolean** | User license status. &#39;true&#39; if user is an individual Power user |  [optional] |
|**lastname** | **String** | Lastname of the user (for education users) |  [optional] |
|**name** | **String** | A displayable name for the user (for consumer users) |  [optional] |
|**picture** | **String** | The URL of the picture to display |  [optional] |
|**printableName** | **String** | The name that can be directly printed (name, firstname &amp; lastname, or username) |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of user account |  [optional] |
|**username** | **String** | The user name (unique for the organization) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| GUEST | &quot;guest&quot; |



