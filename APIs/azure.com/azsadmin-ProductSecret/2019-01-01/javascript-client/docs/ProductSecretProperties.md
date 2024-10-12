# DeploymentAdminClient.ProductSecretProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The secret description. | [optional] 
**expiresAfter** | **String** | The expiration period of the secret (in ISO8601 format). | [optional] 
**provisioningState** | **String** | Provisioning state of the resource. | [optional] 
**secretDescriptor** | [**SecretDescriptor**](SecretDescriptor.md) |  | [optional] 
**secretKind** | **String** | Specifies the secret kind. | [optional] 
**secretState** | [**SecretState**](SecretState.md) |  | [optional] 



## Enum: SecretKindEnum


* `AdHoc` (value: `"AdHoc"`)

* `Certificate` (value: `"Certificate"`)

* `Password` (value: `"Password"`)

* `StorageAccount` (value: `"StorageAccount"`)

* `SymmetricKey` (value: `"SymmetricKey"`)




