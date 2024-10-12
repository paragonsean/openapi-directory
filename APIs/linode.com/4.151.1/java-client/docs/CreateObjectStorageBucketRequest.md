

# CreateObjectStorageBucketRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acl** | [**AclEnum**](#AclEnum) | The Access Control Level of the bucket using a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly.  |  [optional] |
|**cluster** | **String** | The ID of the Object Storage Cluster where this bucket should be created.  |  |
|**corsEnabled** | **Boolean** | If true, the bucket will be created with CORS enabled for all origins. For more fine-grained controls of CORS, use the S3 API directly.  |  [optional] |
|**label** | **String** | The name for this bucket. Must be unique in the cluster you are creating the bucket in, or an error will be returned. Labels will be reserved only for the cluster that active buckets are created and stored in. If you want to reserve this bucket&#39;s label in another cluster, you must create a new bucket with the same label in the new cluster.  |  |



## Enum: AclEnum

| Name | Value |
|---- | -----|
| PRIVATE | &quot;private&quot; |
| PUBLIC_READ | &quot;public-read&quot; |
| AUTHENTICATED_READ | &quot;authenticated-read&quot; |
| PUBLIC_READ_WRITE | &quot;public-read-write&quot; |



