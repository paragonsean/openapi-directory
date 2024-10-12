

# ObjectLevelStatistics

Provides information about the total storage size (in bytes) or number of objects that Amazon Macie can't analyze in one or more S3 buckets. In a BucketMetadata or MatchingBucket object, this data is for a specific bucket. In a GetBucketStatisticsResponse object, this data is aggregated for all the buckets in the query results. If versioning is enabled for a bucket, storage size values are based on the size of the latest version of each applicable object in the bucket.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileType** | [**Integer**](Integer.md) |  |  [optional] |
|**storageClass** | [**Integer**](Integer.md) |  |  [optional] |
|**total** | [**Integer**](Integer.md) |  |  [optional] |



