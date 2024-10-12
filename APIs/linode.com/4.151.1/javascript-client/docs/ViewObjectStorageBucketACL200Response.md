# LinodeApi.ViewObjectStorageBucketACL200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **String** | The Access Control Level of the bucket, as a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly.  | [optional] 
**aclXml** | **String** | The full XML of the object&#39;s ACL policy.  | [optional] 



## Enum: AclEnum


* `private` (value: `"private"`)

* `public-read` (value: `"public-read"`)

* `authenticated-read` (value: `"authenticated-read"`)

* `public-read-write` (value: `"public-read-write"`)

* `custom` (value: `"custom"`)




