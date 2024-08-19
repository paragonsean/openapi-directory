

# S3InitiateRestoreObjectOperation

Contains the configuration parameters for a POST Object restore job. S3 Batch Operations passes every object to the underlying <code>RestoreObject</code> API operation. For more information about the parameters for this operation, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOSTrestore.html#RESTObjectPOSTrestore-restore-request\">RestoreObject</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationInDays** | [**Integer**](Integer.md) |  |  [optional] |
|**glacierJobTier** | [**S3GlacierJobTier**](S3GlacierJobTier.md) |  |  [optional] |



