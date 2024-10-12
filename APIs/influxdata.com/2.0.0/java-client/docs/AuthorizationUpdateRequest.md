

# AuthorizationUpdateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the token. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | If inactive the token is inactive and requests using the token will be rejected. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



