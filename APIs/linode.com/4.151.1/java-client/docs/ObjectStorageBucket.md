

# ObjectStorageBucket

An Object Storage Bucket. This should be accessed primarily through the S3 API; [click here for more information](https://docs.ceph.com/en/latest/radosgw/s3/#api). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cluster** | **String** | The ID of the Object Storage Cluster this bucket is in. |  [optional] |
|**created** | **OffsetDateTime** | When this bucket was created. |  [optional] |
|**hostname** | **String** | The hostname where this bucket can be accessed. This hostname can be accessed through a browser if the bucket is made public.  |  [optional] |
|**label** | **String** | The name of this bucket. |  [optional] |
|**objects** | **Integer** | The number of objects stored in this bucket.  |  [optional] |
|**size** | **Integer** | The size of the bucket in bytes. |  [optional] |



