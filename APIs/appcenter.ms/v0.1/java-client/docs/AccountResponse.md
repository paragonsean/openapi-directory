

# AccountResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The display name of the account |  |
|**email** | **String** | The account&#39;s email. For org that value might be empty. |  [optional] |
|**id** | **UUID** | The internal unique id (UUID) of the account. |  |
|**name** | **String** | The slug name of the account |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this account |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this account |  |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| ORG | &quot;org&quot; |



