

# ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjects

Files in the workspace to upload to Cloud Storage upon successful completion of all build steps.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | Cloud Storage bucket and optional object path, in the form \&quot;gs://bucket/path/to/somewhere/\&quot;. (see [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)). Files in the workspace matching any path pattern will be uploaded to Cloud Storage with this location as a prefix. |  [optional] |
|**paths** | **List&lt;String&gt;** | Path globs used to match files in the build&#39;s workspace. |  [optional] |
|**timing** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan**](ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan.md) |  |  [optional] |



