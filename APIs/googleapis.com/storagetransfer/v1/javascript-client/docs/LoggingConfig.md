# StorageTransferApi.LoggingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableOnpremGcsTransferLogs** | **Boolean** | For transfers with a PosixFilesystem source, this option enables the Cloud Storage transfer logs for this transfer. | [optional] 
**logActionStates** | **[String]** | States in which &#x60;log_actions&#x60; are logged. If empty, no logs are generated. Not supported for transfers with PosixFilesystem data sources; use enable_onprem_gcs_transfer_logs instead. | [optional] 
**logActions** | **[String]** | Specifies the actions to be logged. If empty, no logs are generated. Not supported for transfers with PosixFilesystem data sources; use enable_onprem_gcs_transfer_logs instead. | [optional] 



## Enum: [LogActionStatesEnum]


* `LOGGABLE_ACTION_STATE_UNSPECIFIED` (value: `"LOGGABLE_ACTION_STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)





## Enum: [LogActionsEnum]


* `LOGGABLE_ACTION_UNSPECIFIED` (value: `"LOGGABLE_ACTION_UNSPECIFIED"`)

* `FIND` (value: `"FIND"`)

* `DELETE` (value: `"DELETE"`)

* `COPY` (value: `"COPY"`)




