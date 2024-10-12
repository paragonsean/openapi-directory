

# TokenPassword

The password that will be used for authenticating the token of a container registry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | The creation datetime of the password. |  [optional] |
|**expiry** | **OffsetDateTime** | The expiry datetime of the password. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | The password name \&quot;password1\&quot; or \&quot;password2\&quot; |  [optional] |
|**value** | **String** | The password value. |  [optional] [readonly] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| PASSWORD1 | &quot;password1&quot; |
| PASSWORD2 | &quot;password2&quot; |



