

# Authorization


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the token. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | If inactive the token is inactive and requests using the token will be rejected. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**id** | **String** |  |  [optional] [readonly] |
|**links** | [**AuthorizationAllOfLinks**](AuthorizationAllOfLinks.md) |  |  [optional] |
|**org** | **String** | Name of the org token is scoped to. |  [optional] [readonly] |
|**orgID** | **String** | ID of org that authorization is scoped to. |  |
|**permissions** | [**List&lt;Permission&gt;**](Permission.md) | List of permissions for an auth.  An auth must have at least one Permission. |  |
|**token** | **String** | Passed via the Authorization Header and Token Authentication type. |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**user** | **String** | Name of user that created and owns the token. |  [optional] [readonly] |
|**userID** | **String** | ID of user that created and owns the token. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



