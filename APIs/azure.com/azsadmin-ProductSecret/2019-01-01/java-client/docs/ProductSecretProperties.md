

# ProductSecretProperties

Properties of product secret.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The secret description. |  [optional] |
|**expiresAfter** | **String** | The expiration period of the secret (in ISO8601 format). |  [optional] |
|**provisioningState** | **String** | Provisioning state of the resource. |  [optional] |
|**secretDescriptor** | [**SecretDescriptor**](SecretDescriptor.md) |  |  [optional] |
|**secretKind** | [**SecretKindEnum**](#SecretKindEnum) | Specifies the secret kind. |  [optional] |
|**secretState** | [**SecretState**](SecretState.md) |  |  [optional] |



## Enum: SecretKindEnum

| Name | Value |
|---- | -----|
| AD_HOC | &quot;AdHoc&quot; |
| CERTIFICATE | &quot;Certificate&quot; |
| PASSWORD | &quot;Password&quot; |
| STORAGE_ACCOUNT | &quot;StorageAccount&quot; |
| SYMMETRIC_KEY | &quot;SymmetricKey&quot; |



