

# ResourceMember


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] [readonly] |
|**links** | [**UserResponseLinks**](UserResponseLinks.md) |  |  [optional] |
|**name** | **String** |  |  |
|**oauthID** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | If inactive the user is inactive. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| MEMBER | &quot;member&quot; |



