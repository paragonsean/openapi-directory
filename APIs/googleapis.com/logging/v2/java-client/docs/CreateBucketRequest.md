

# CreateBucketRequest

The parameters to CreateBucket.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucket** | [**LogBucket**](LogBucket.md) |  |  [optional] |
|**bucketId** | **String** | Required. A client-assigned identifier such as \&quot;my-bucket\&quot;. Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. |  [optional] |
|**parent** | **String** | Required. The resource in which to create the log bucket: \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]\&quot; For example:\&quot;projects/my-project/locations/global\&quot; |  [optional] |



