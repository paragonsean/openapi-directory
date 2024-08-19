

# JobError

Details of JobOutput errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | Helps with categorization of errors. |  [optional] [readonly] |
|**code** | [**CodeEnum**](#CodeEnum) | Error code describing the error. |  [optional] [readonly] |
|**details** | [**List&lt;JobErrorDetail&gt;**](JobErrorDetail.md) | An array of details about specific errors that led to this reported error. |  [optional] [readonly] |
|**message** | **String** | A human-readable language-dependent representation of the error. |  [optional] [readonly] |
|**retry** | [**RetryEnum**](#RetryEnum) | Indicates that it may be possible to retry the Job. If retry is unsuccessful, please contact Azure support via Azure Portal. |  [optional] [readonly] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| SERVICE | &quot;Service&quot; |
| DOWNLOAD | &quot;Download&quot; |
| UPLOAD | &quot;Upload&quot; |
| CONFIGURATION | &quot;Configuration&quot; |
| CONTENT | &quot;Content&quot; |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| SERVICE_ERROR | &quot;ServiceError&quot; |
| SERVICE_TRANSIENT_ERROR | &quot;ServiceTransientError&quot; |
| DOWNLOAD_NOT_ACCESSIBLE | &quot;DownloadNotAccessible&quot; |
| DOWNLOAD_TRANSIENT_ERROR | &quot;DownloadTransientError&quot; |
| UPLOAD_NOT_ACCESSIBLE | &quot;UploadNotAccessible&quot; |
| UPLOAD_TRANSIENT_ERROR | &quot;UploadTransientError&quot; |
| CONFIGURATION_UNSUPPORTED | &quot;ConfigurationUnsupported&quot; |
| CONTENT_MALFORMED | &quot;ContentMalformed&quot; |
| CONTENT_UNSUPPORTED | &quot;ContentUnsupported&quot; |



## Enum: RetryEnum

| Name | Value |
|---- | -----|
| DO_NOT_RETRY | &quot;DoNotRetry&quot; |
| MAY_RETRY | &quot;MayRetry&quot; |



