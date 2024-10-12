

# UpdateObjectStorageBucketACLRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acl** | [**AclEnum**](#AclEnum) | The Access Control Level of the bucket, as a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly.  |  |
|**name** | **String** | The &#x60;name&#x60; of the object for which to update its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket.  |  |



## Enum: AclEnum

| Name | Value |
|---- | -----|
| PRIVATE | &quot;private&quot; |
| PUBLIC_READ | &quot;public-read&quot; |
| AUTHENTICATED_READ | &quot;authenticated-read&quot; |
| PUBLIC_READ_WRITE | &quot;public-read-write&quot; |
| CUSTOM | &quot;custom&quot; |



