

# ExportServerSideEncryption

Encryption configuration of the export job. Includes the encryption type in addition to the AWS KMS key. The KMS key is only necessary if you chose the KMS encryption type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyArn** | [**String**](String.md) |  |  [optional] |
|**type** | [**ServerSideEncryptionTypes**](ServerSideEncryptionTypes.md) |  |  |



