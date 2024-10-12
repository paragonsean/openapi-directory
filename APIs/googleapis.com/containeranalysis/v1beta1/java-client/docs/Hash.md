

# Hash

Container message for hash values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of hash that was performed. |  [optional] |
|**value** | **byte[]** | Required. The hash value. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HASH_TYPE_UNSPECIFIED | &quot;HASH_TYPE_UNSPECIFIED&quot; |
| SHA256 | &quot;SHA256&quot; |
| GO_MODULE_H1 | &quot;GO_MODULE_H1&quot; |
| SHA512 | &quot;SHA512&quot; |



