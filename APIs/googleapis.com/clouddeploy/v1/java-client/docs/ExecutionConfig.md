

# ExecutionConfig

Configuration of the environment to use when calling Skaffold.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactStorage** | **String** | Optional. Cloud Storage location in which to store execution outputs. This can either be a bucket (\&quot;gs://my-bucket\&quot;) or a path within a bucket (\&quot;gs://my-bucket/my-dir\&quot;). If unspecified, a default bucket located in the same region will be used. |  [optional] |
|**defaultPool** | [**DefaultPool**](DefaultPool.md) |  |  [optional] |
|**executionTimeout** | **String** | Optional. Execution timeout for a Cloud Build Execution. This must be between 10m and 24h in seconds format. If unspecified, a default timeout of 1h is used. |  [optional] |
|**privatePool** | [**PrivatePool**](PrivatePool.md) |  |  [optional] |
|**serviceAccount** | **String** | Optional. Google service account to use for execution. If unspecified, the project execution service account (-compute@developer.gserviceaccount.com) is used. |  [optional] |
|**usages** | [**List&lt;UsagesEnum&gt;**](#List&lt;UsagesEnum&gt;) | Required. Usages when this configuration should be applied. |  [optional] |
|**workerPool** | **String** | Optional. The resource name of the &#x60;WorkerPool&#x60;, with the format &#x60;projects/{project}/locations/{location}/workerPools/{worker_pool}&#x60;. If this optional field is unspecified, the default Cloud Build pool will be used. |  [optional] |



## Enum: List&lt;UsagesEnum&gt;

| Name | Value |
|---- | -----|
| EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED | &quot;EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED&quot; |
| RENDER | &quot;RENDER&quot; |
| DEPLOY | &quot;DEPLOY&quot; |
| VERIFY | &quot;VERIFY&quot; |
| PREDEPLOY | &quot;PREDEPLOY&quot; |
| POSTDEPLOY | &quot;POSTDEPLOY&quot; |



