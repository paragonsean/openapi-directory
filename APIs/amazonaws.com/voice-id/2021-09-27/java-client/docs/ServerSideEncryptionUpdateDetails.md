

# ServerSideEncryptionUpdateDetails

Details about the most recent server-side encryption configuration update. When the server-side encryption configuration is changed, dependency on the old KMS key is removed through an asynchronous process. When this update is complete, the domain’s data can only be accessed using the new KMS key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**String**](String.md) |  |  [optional] |
|**oldKmsKeyId** | [**String**](String.md) |  |  [optional] |
|**updateStatus** | [**ServerSideEncryptionUpdateStatus**](ServerSideEncryptionUpdateStatus.md) |  |  [optional] |



