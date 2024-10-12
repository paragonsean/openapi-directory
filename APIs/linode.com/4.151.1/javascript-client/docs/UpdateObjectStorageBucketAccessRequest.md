# LinodeApi.UpdateObjectStorageBucketAccessRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **String** | The Access Control Level of the bucket, as a canned ACL string. For more fine-grained control of ACLs, use the S3 API directly.  | [optional] 
**corsEnabled** | **Boolean** | If true, the bucket will be created with CORS enabled for all origins. For more fine-grained controls of CORS, use the S3 API directly.  | [optional] 



## Enum: AclEnum


* `private` (value: `"private"`)

* `public-read` (value: `"public-read"`)

* `authenticated-read` (value: `"authenticated-read"`)

* `public-read-write` (value: `"public-read-write"`)

* `custom` (value: `"custom"`)




