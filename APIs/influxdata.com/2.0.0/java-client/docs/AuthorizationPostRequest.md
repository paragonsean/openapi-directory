

# AuthorizationPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the token. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | If inactive the token is inactive and requests using the token will be rejected. |  [optional] |
|**orgID** | **String** | ID of org that authorization is scoped to. |  |
|**permissions** | [**List&lt;Permission&gt;**](Permission.md) | List of permissions for an auth.  An auth must have at least one Permission. |  |
|**userID** | **String** | ID of user that authorization is scoped to. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



