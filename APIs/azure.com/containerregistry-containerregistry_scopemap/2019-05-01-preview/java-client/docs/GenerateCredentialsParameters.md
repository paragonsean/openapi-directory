

# GenerateCredentialsParameters

The parameters used to generate credentials for a specified token or user of a container registry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiry** | **OffsetDateTime** | The expiry date of the generated credentials after which the credentials become invalid. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | Specifies name of the password which should be regenerated if any -- password1 or password2. |  [optional] |
|**tokenId** | **String** | The resource ID of the token for which credentials have to be generated. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| PASSWORD1 | &quot;password1&quot; |
| PASSWORD2 | &quot;password2&quot; |



