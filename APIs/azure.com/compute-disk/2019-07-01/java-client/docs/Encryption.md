

# Encryption

Encryption at rest settings for disk or snapshot

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskEncryptionSetId** | **String** | ResourceId of the disk encryption set to use for enabling encryption at rest. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of key used to encrypt the data of the disk. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ENCRYPTION_AT_REST_WITH_PLATFORM_KEY | &quot;EncryptionAtRestWithPlatformKey&quot; |
| ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY | &quot;EncryptionAtRestWithCustomerKey&quot; |



