

# SkaffoldGCSSource

Cloud Storage bucket containing Skaffold Config modules.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**path** | **String** | Optional. Relative path from the source to the Skaffold file. |  [optional] |
|**source** | **String** | Required. Cloud Storage source paths to copy recursively. For example, providing \&quot;gs://my-bucket/dir/configs/_*\&quot; will result in Skaffold copying all files within the \&quot;dir/configs\&quot; directory in the bucket \&quot;my-bucket\&quot;. |  [optional] |



