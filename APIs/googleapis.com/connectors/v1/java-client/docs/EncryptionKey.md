

# EncryptionKey

Encryption Key value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyName** | **String** | The [KMS key name] with which the content of the Operation is encrypted. The expected format: &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*&#x60;. Will be empty string if google managed. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GOOGLE_MANAGED | &quot;GOOGLE_MANAGED&quot; |
| CUSTOMER_MANAGED | &quot;CUSTOMER_MANAGED&quot; |



