# AwsIoTSiteWise.PutDefaultEncryptionConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionType** | **String** | The type of encryption used for the encryption configuration. | 
**kmsKeyId** | **String** | The Key ID of the customer managed key used for KMS encryption. This is required if you use &lt;code&gt;KMS_BASED_ENCRYPTION&lt;/code&gt;. | [optional] 



## Enum: EncryptionTypeEnum


* `SITEWISE_DEFAULT_ENCRYPTION` (value: `"SITEWISE_DEFAULT_ENCRYPTION"`)

* `KMS_BASED_ENCRYPTION` (value: `"KMS_BASED_ENCRYPTION"`)




