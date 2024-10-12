

# ViewObjectStorageBucketACL200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acl** | [**AclEnum**](#AclEnum) | The Access Control Level of the bucket, as a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly.  |  [optional] |
|**aclXml** | **String** | The full XML of the object&#39;s ACL policy.  |  [optional] |



## Enum: AclEnum

| Name | Value |
|---- | -----|
| PRIVATE | &quot;private&quot; |
| PUBLIC_READ | &quot;public-read&quot; |
| AUTHENTICATED_READ | &quot;authenticated-read&quot; |
| PUBLIC_READ_WRITE | &quot;public-read-write&quot; |
| CUSTOM | &quot;custom&quot; |



