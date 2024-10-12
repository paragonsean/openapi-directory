

# Bucket

A bucket.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acl** | [**List&lt;BucketAccessControl&gt;**](BucketAccessControl.md) | Access controls on the bucket. |  [optional] |
|**cors** | [**List&lt;BucketCorsInner&gt;**](BucketCorsInner.md) | The bucket&#39;s Cross-Origin Resource Sharing (CORS) configuration. |  [optional] |
|**defaultObjectAcl** | [**List&lt;ObjectAccessControl&gt;**](ObjectAccessControl.md) | Default access controls to apply to new objects when no ACL is provided. |  [optional] |
|**etag** | **String** | HTTP 1.1 Entity tag for the bucket. |  [optional] |
|**id** | **String** | The ID of the bucket. |  [optional] |
|**kind** | **String** | The kind of item this is. For buckets, this is always storage#bucket. |  [optional] |
|**lifecycle** | [**BucketLifecycle**](BucketLifecycle.md) |  |  [optional] |
|**location** | **String** | The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Typical values are US and EU. Defaults to US. See the developer&#39;s guide for the authoritative list. |  [optional] |
|**logging** | [**BucketLogging**](BucketLogging.md) |  |  [optional] |
|**metageneration** | **String** | The metadata generation of this bucket. |  [optional] |
|**name** | **String** | The name of the bucket. |  [optional] |
|**owner** | [**BucketOwner**](BucketOwner.md) |  |  [optional] |
|**selfLink** | **String** | The URI of this bucket. |  [optional] |
|**storageClass** | **String** | The bucket&#39;s storage class. This defines how objects in the bucket are stored and determines the SLA and the cost of storage. Typical values are STANDARD and DURABLE_REDUCED_AVAILABILITY. Defaults to STANDARD. See the developer&#39;s guide for the authoritative list. |  [optional] |
|**timeCreated** | **OffsetDateTime** | Creation time of the bucket in RFC 3339 format. |  [optional] |
|**versioning** | [**BucketVersioning**](BucketVersioning.md) |  |  [optional] |
|**website** | [**BucketWebsite**](BucketWebsite.md) |  |  [optional] |



