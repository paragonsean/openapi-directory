

# LoggingConfig

Specifies the logging behavior for transfer operations. For cloud-to-cloud transfers, logs are sent to Cloud Logging. See [Read transfer logs](https://cloud.google.com/storage-transfer/docs/read-transfer-logs) for details. For transfers to or from a POSIX file system, logs are stored in the Cloud Storage bucket that is the source or sink of the transfer. See [Managing Transfer for on-premises jobs] (https://cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#viewing-logs) for details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableOnpremGcsTransferLogs** | **Boolean** | For transfers with a PosixFilesystem source, this option enables the Cloud Storage transfer logs for this transfer. |  [optional] |
|**logActionStates** | [**List&lt;LogActionStatesEnum&gt;**](#List&lt;LogActionStatesEnum&gt;) | States in which &#x60;log_actions&#x60; are logged. If empty, no logs are generated. Not supported for transfers with PosixFilesystem data sources; use enable_onprem_gcs_transfer_logs instead. |  [optional] |
|**logActions** | [**List&lt;LogActionsEnum&gt;**](#List&lt;LogActionsEnum&gt;) | Specifies the actions to be logged. If empty, no logs are generated. Not supported for transfers with PosixFilesystem data sources; use enable_onprem_gcs_transfer_logs instead. |  [optional] |



## Enum: List&lt;LogActionStatesEnum&gt;

| Name | Value |
|---- | -----|
| LOGGABLE_ACTION_STATE_UNSPECIFIED | &quot;LOGGABLE_ACTION_STATE_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: List&lt;LogActionsEnum&gt;

| Name | Value |
|---- | -----|
| LOGGABLE_ACTION_UNSPECIFIED | &quot;LOGGABLE_ACTION_UNSPECIFIED&quot; |
| FIND | &quot;FIND&quot; |
| DELETE | &quot;DELETE&quot; |
| COPY | &quot;COPY&quot; |



