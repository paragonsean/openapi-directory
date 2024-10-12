

# AwsS3CompatibleData

An AwsS3CompatibleData resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketName** | **String** | Required. Specifies the name of the bucket. |  [optional] |
|**endpoint** | **String** | Required. Specifies the endpoint of the storage service. |  [optional] |
|**path** | **String** | Specifies the root path to transfer objects. Must be an empty string or full path name that ends with a &#39;/&#39;. This field is treated as an object prefix. As such, it should generally not begin with a &#39;/&#39;. |  [optional] |
|**region** | **String** | Specifies the region to sign requests with. This can be left blank if requests should be signed with an empty region. |  [optional] |
|**s3Metadata** | [**S3CompatibleMetadata**](S3CompatibleMetadata.md) |  |  [optional] |



