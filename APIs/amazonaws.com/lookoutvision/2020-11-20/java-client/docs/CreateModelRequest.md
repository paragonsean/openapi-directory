

# CreateModelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description for the version of the model. |  [optional] |
|**outputConfig** | [**CreateModelRequestOutputConfig**](CreateModelRequestOutputConfig.md) |  |  |
|**kmsKeyId** | **String** | The identifier for your AWS KMS key. The key is used to encrypt training and test images copied into the service for model training. Your source images are unaffected. If this parameter is not specified, the copied images are encrypted by a key that AWS owns and manages. |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A set of tags (key-value pairs) that you want to attach to the model. |  [optional] |



