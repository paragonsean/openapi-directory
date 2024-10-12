

# Detection

Provides information about a type of sensitive data that Amazon Macie found in an S3 bucket while performing automated sensitive data discovery for the bucket. The information also specifies the custom data identifier or managed data identifier that detected the data. This information is available only if automated sensitive data discovery is currently enabled for your account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**count** | [**Integer**](Integer.md) |  |  [optional] |
|**id** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**suppressed** | [**Boolean**](Boolean.md) |  |  [optional] |
|**type** | [**DataIdentifierType**](DataIdentifierType.md) |  |  [optional] |



