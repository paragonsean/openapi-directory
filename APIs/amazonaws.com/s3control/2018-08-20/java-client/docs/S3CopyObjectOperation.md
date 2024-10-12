

# S3CopyObjectOperation

Contains the configuration parameters for a PUT Copy object operation. S3 Batch Operations passes every object to the underlying <code>CopyObject</code> API operation. For more information about the parameters for this operation, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectCOPY.html\">CopyObject</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetResource** | [**String**](String.md) |  |  [optional] |
|**cannedAccessControlList** | [**S3CannedAccessControlList**](S3CannedAccessControlList.md) |  |  [optional] |
|**accessControlGrants** | [**List**](List.md) |  |  [optional] |
|**metadataDirective** | [**S3MetadataDirective**](S3MetadataDirective.md) |  |  [optional] |
|**modifiedSinceConstraint** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**newObjectMetadata** | [**S3CopyObjectOperationNewObjectMetadata**](S3CopyObjectOperationNewObjectMetadata.md) |  |  [optional] |
|**newObjectTagging** | [**List**](List.md) |  |  [optional] |
|**redirectLocation** | [**String**](String.md) |  |  [optional] |
|**requesterPays** | [**Boolean**](Boolean.md) |  |  [optional] |
|**storageClass** | [**S3StorageClass**](S3StorageClass.md) |  |  [optional] |
|**unModifiedSinceConstraint** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**ssEAwsKmsKeyId** | [**String**](String.md) |  |  [optional] |
|**targetKeyPrefix** | [**String**](String.md) |  |  [optional] |
|**objectLockLegalHoldStatus** | [**S3ObjectLockLegalHoldStatus**](S3ObjectLockLegalHoldStatus.md) |  |  [optional] |
|**objectLockMode** | [**S3ObjectLockMode**](S3ObjectLockMode.md) |  |  [optional] |
|**objectLockRetainUntilDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**bucketKeyEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**checksumAlgorithm** | [**S3ChecksumAlgorithm**](S3ChecksumAlgorithm.md) |  |  [optional] |



