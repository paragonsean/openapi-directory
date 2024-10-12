

# Policy

A bucket/object/managedFolder IAM policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bindings** | [**List&lt;PolicyBindingsInner&gt;**](PolicyBindingsInner.md) | An association between a role, which comes with a set of permissions, and members who may assume that role. |  [optional] |
|**etag** | **byte[]** | HTTP 1.1  Entity tag for the policy. |  [optional] |
|**kind** | **String** | The kind of item this is. For policies, this is always storage#policy. This field is ignored on input. |  [optional] |
|**resourceId** | **String** | The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, projects/_/buckets/bucket/objects/object for objects, and projects/_/buckets/bucket/managedFolders/managedFolder. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input. |  [optional] |
|**version** | **Integer** | The IAM policy format version. |  [optional] |



