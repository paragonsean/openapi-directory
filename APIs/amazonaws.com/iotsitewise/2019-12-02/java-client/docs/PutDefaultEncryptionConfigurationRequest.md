

# PutDefaultEncryptionConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionType** | [**EncryptionTypeEnum**](#EncryptionTypeEnum) | The type of encryption used for the encryption configuration. |  |
|**kmsKeyId** | **String** | The Key ID of the customer managed key used for KMS encryption. This is required if you use &lt;code&gt;KMS_BASED_ENCRYPTION&lt;/code&gt;. |  [optional] |



## Enum: EncryptionTypeEnum

| Name | Value |
|---- | -----|
| SITEWISE_DEFAULT_ENCRYPTION | &quot;SITEWISE_DEFAULT_ENCRYPTION&quot; |
| KMS_BASED_ENCRYPTION | &quot;KMS_BASED_ENCRYPTION&quot; |



