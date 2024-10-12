

# MatchingBucket

<p>Provides statistical data and other information about an S3 bucket that Amazon Macie monitors and analyzes for your account. By default, object count and storage size values include data for object parts that are the result of incomplete multipart uploads. For more information, see <a href=\"https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html\">How Macie monitors Amazon S3 data security</a> in the <i>Amazon Macie User Guide</i>.</p> <p>If an error occurs when Macie attempts to retrieve and process information about the bucket or the bucket's objects, the value for most of these properties is null. Key exceptions are accountId and bucketName. To identify the cause of the error, refer to the errorCode and errorMessage values.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | [**String**](String.md) |  |  [optional] |
|**bucketName** | [**String**](String.md) |  |  [optional] |
|**classifiableObjectCount** | [**Integer**](Integer.md) |  |  [optional] |
|**classifiableSizeInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**errorCode** | [**BucketMetadataErrorCode**](BucketMetadataErrorCode.md) |  |  [optional] |
|**errorMessage** | [**String**](String.md) |  |  [optional] |
|**jobDetails** | [**MatchingBucketJobDetails**](MatchingBucketJobDetails.md) |  |  [optional] |
|**lastAutomatedDiscoveryTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**objectCount** | [**Integer**](Integer.md) |  |  [optional] |
|**objectCountByEncryptionType** | [**BucketMetadataObjectCountByEncryptionType**](BucketMetadataObjectCountByEncryptionType.md) |  |  [optional] |
|**sensitivityScore** | [**Integer**](Integer.md) |  |  [optional] |
|**sizeInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**sizeInBytesCompressed** | [**Integer**](Integer.md) |  |  [optional] |
|**unclassifiableObjectCount** | [**BucketMetadataUnclassifiableObjectCount**](BucketMetadataUnclassifiableObjectCount.md) |  |  [optional] |
|**unclassifiableObjectSizeInBytes** | [**BucketMetadataUnclassifiableObjectSizeInBytes**](BucketMetadataUnclassifiableObjectSizeInBytes.md) |  |  [optional] |



