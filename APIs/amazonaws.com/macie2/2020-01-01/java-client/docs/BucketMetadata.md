

# BucketMetadata

<p>Provides statistical data and other information about an S3 bucket that Amazon Macie monitors and analyzes for your account. By default, object count and storage size values include data for object parts that are the result of incomplete multipart uploads. For more information, see <a href=\"https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html\">How Macie monitors Amazon S3 data security</a> in the <i>Amazon Macie User Guide</i>.</p> <p>If an error occurs when Macie attempts to retrieve and process metadata from Amazon S3 for the bucket or the bucket's objects, the value for the versioning property is false and the value for most other properties is null. Key exceptions are accountId, bucketArn, bucketCreatedAt, bucketName, lastUpdated, and region. To identify the cause of the error, refer to the errorCode and errorMessage values.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | [**String**](String.md) |  |  [optional] |
|**allowsUnencryptedObjectUploads** | [**AllowsUnencryptedObjectUploads**](AllowsUnencryptedObjectUploads.md) |  |  [optional] |
|**bucketArn** | [**String**](String.md) |  |  [optional] |
|**bucketCreatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**bucketName** | [**String**](String.md) |  |  [optional] |
|**classifiableObjectCount** | [**Integer**](Integer.md) |  |  [optional] |
|**classifiableSizeInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**errorCode** | [**BucketMetadataErrorCode**](BucketMetadataErrorCode.md) |  |  [optional] |
|**errorMessage** | [**String**](String.md) |  |  [optional] |
|**jobDetails** | [**BucketMetadataJobDetails**](BucketMetadataJobDetails.md) |  |  [optional] |
|**lastAutomatedDiscoveryTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdated** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**objectCount** | [**Integer**](Integer.md) |  |  [optional] |
|**objectCountByEncryptionType** | [**BucketMetadataObjectCountByEncryptionType**](BucketMetadataObjectCountByEncryptionType.md) |  |  [optional] |
|**publicAccess** | [**BucketMetadataPublicAccess**](BucketMetadataPublicAccess.md) |  |  [optional] |
|**region** | [**String**](String.md) |  |  [optional] |
|**replicationDetails** | [**BucketMetadataReplicationDetails**](BucketMetadataReplicationDetails.md) |  |  [optional] |
|**sensitivityScore** | [**Integer**](Integer.md) |  |  [optional] |
|**serverSideEncryption** | [**BucketMetadataServerSideEncryption**](BucketMetadataServerSideEncryption.md) |  |  [optional] |
|**sharedAccess** | [**SharedAccess**](SharedAccess.md) |  |  [optional] |
|**sizeInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**sizeInBytesCompressed** | [**Integer**](Integer.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**unclassifiableObjectCount** | [**BucketMetadataUnclassifiableObjectCount**](BucketMetadataUnclassifiableObjectCount.md) |  |  [optional] |
|**unclassifiableObjectSizeInBytes** | [**BucketMetadataUnclassifiableObjectSizeInBytes**](BucketMetadataUnclassifiableObjectSizeInBytes.md) |  |  [optional] |
|**versioning** | [**Boolean**](Boolean.md) |  |  [optional] |



