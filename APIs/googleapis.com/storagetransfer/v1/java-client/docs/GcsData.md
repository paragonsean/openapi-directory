

# GcsData

In a GcsData resource, an object's name is the Cloud Storage object's name and its \"last modification time\" refers to the object's `updated` property of Cloud Storage objects, which changes when the content or the metadata of the object is updated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketName** | **String** | Required. Cloud Storage bucket name. Must meet [Bucket Name Requirements](/storage/docs/naming#requirements). |  [optional] |
|**managedFolderTransferEnabled** | **Boolean** | Transfer managed folders is in public preview. This option is only applicable to the Cloud Storage source bucket. If set to true: - The source managed folder will be transferred to the destination bucket - The destination managed folder will always be overwritten, other OVERWRITE options will not be supported |  [optional] |
|**path** | **String** | Root path to transfer objects. Must be an empty string or full path name that ends with a &#39;/&#39;. This field is treated as an object prefix. As such, it should generally not begin with a &#39;/&#39;. The root path value must meet [Object Name Requirements](/storage/docs/naming#objectnames). |  [optional] |



