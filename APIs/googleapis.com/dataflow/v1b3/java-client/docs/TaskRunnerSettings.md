

# TaskRunnerSettings

Taskrunner configuration settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alsologtostderr** | **Boolean** | Whether to also send taskrunner log info to stderr. |  [optional] |
|**baseTaskDir** | **String** | The location on the worker for task-specific subdirectories. |  [optional] |
|**baseUrl** | **String** | The base URL for the taskrunner to use when accessing Google Cloud APIs. When workers access Google Cloud APIs, they logically do so via relative URLs. If this field is specified, it supplies the base URL to use for resolving these relative URLs. The normative algorithm used is defined by RFC 1808, \&quot;Relative Uniform Resource Locators\&quot;. If not specified, the default value is \&quot;http://www.googleapis.com/\&quot; |  [optional] |
|**commandlinesFileName** | **String** | The file to store preprocessing commands in. |  [optional] |
|**continueOnException** | **Boolean** | Whether to continue taskrunner if an exception is hit. |  [optional] |
|**dataflowApiVersion** | **String** | The API version of endpoint, e.g. \&quot;v1b3\&quot; |  [optional] |
|**harnessCommand** | **String** | The command to launch the worker harness. |  [optional] |
|**languageHint** | **String** | The suggested backend language. |  [optional] |
|**logDir** | **String** | The directory on the VM to store logs. |  [optional] |
|**logToSerialconsole** | **Boolean** | Whether to send taskrunner log info to Google Compute Engine VM serial console. |  [optional] |
|**logUploadLocation** | **String** | Indicates where to put logs. If this is not specified, the logs will not be uploaded. The supported resource type is: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} |  [optional] |
|**oauthScopes** | **List&lt;String&gt;** | The OAuth2 scopes to be requested by the taskrunner in order to access the Cloud Dataflow API. |  [optional] |
|**parallelWorkerSettings** | [**WorkerSettings**](WorkerSettings.md) |  |  [optional] |
|**streamingWorkerMainClass** | **String** | The streaming worker main class name. |  [optional] |
|**taskGroup** | **String** | The UNIX group ID on the worker VM to use for tasks launched by taskrunner; e.g. \&quot;wheel\&quot;. |  [optional] |
|**taskUser** | **String** | The UNIX user ID on the worker VM to use for tasks launched by taskrunner; e.g. \&quot;root\&quot;. |  [optional] |
|**tempStoragePrefix** | **String** | The prefix of the resources the taskrunner should use for temporary storage. The supported resource type is: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} |  [optional] |
|**vmId** | **String** | The ID string of the VM. |  [optional] |
|**workflowFileName** | **String** | The file to store the workflow in. |  [optional] |



