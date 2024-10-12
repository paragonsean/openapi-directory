

# WorkerSettings

Provides data to pass through to the worker harness.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseUrl** | **String** | The base URL for accessing Google Cloud APIs. When workers access Google Cloud APIs, they logically do so via relative URLs. If this field is specified, it supplies the base URL to use for resolving these relative URLs. The normative algorithm used is defined by RFC 1808, \&quot;Relative Uniform Resource Locators\&quot;. If not specified, the default value is \&quot;http://www.googleapis.com/\&quot; |  [optional] |
|**reportingEnabled** | **Boolean** | Whether to send work progress updates to the service. |  [optional] |
|**servicePath** | **String** | The Cloud Dataflow service path relative to the root URL, for example, \&quot;dataflow/v1b3/projects\&quot;. |  [optional] |
|**shuffleServicePath** | **String** | The Shuffle service path relative to the root URL, for example, \&quot;shuffle/v1beta1\&quot;. |  [optional] |
|**tempStoragePrefix** | **String** | The prefix of the resources the system should use for temporary storage. The supported resource type is: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} |  [optional] |
|**workerId** | **String** | The ID of the worker running this pipeline. |  [optional] |



