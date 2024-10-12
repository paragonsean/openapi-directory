

# UserAuthResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The full name of the user. Might for example be first and last name |  |
|**email** | **String** | The email address of the user |  |
|**externalProvider** | **String** | The name of the external auth provider |  [optional] |
|**externalUserId** | **String** | The user ID given by the external provider |  [optional] |
|**id** | **UUID** | The unique id (UUID) of the user |  |
|**name** | **String** | The unique name that is used to identify the user |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this user |  |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |
| CODEPUSH | &quot;codepush&quot; |



