

# SecretObject

Describes the properties of a secret object value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of the secret object which determines how the value of the secret object has to be  interpreted. |  [optional] |
|**value** | **String** | The value of the secret. The format of this value will be determined  based on the type of the secret object. If the type is Opaque, the value will be  used as is without any modification. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OPAQUE | &quot;Opaque&quot; |
| VAULTSECRET | &quot;Vaultsecret&quot; |



