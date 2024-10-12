

# InlinedValueSecretResourceProperties

Describes the properties of a secret resource whose value is provided explicitly as plaintext. The secret resource may have multiple values, each being uniquely versioned. The secret value of each version is stored encrypted, and delivered as plaintext into the context of applications referencing it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | **String** | The type of the content stored in the secret value. The value of this property is opaque to Service Fabric. Once set, the value of this property cannot be changed. |  [optional] |
|**description** | **String** | User readable description of the secret. |  [optional] |
|**status** | **ResourceStatus** |  |  [optional] |
|**statusDetails** | **String** | Gives additional information about the current status of the secret. |  [optional] [readonly] |
|**kind** | **SecretKind** |  |  |
|**provisioningState** | **String** | State of the resource. |  [optional] [readonly] |



