# DataflowApi.WorkerLifecycleEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerStartTime** | **String** | The start time of this container. All events will report this so that events can be grouped together across container/VM restarts. | [optional] 
**event** | **String** | The event being reported. | [optional] 
**metadata** | **{String: String}** | Other stats that can accompany an event. E.g. { \&quot;downloaded_bytes\&quot; : \&quot;123456\&quot; } | [optional] 



## Enum: EventEnum


* `UNKNOWN_EVENT` (value: `"UNKNOWN_EVENT"`)

* `OS_START` (value: `"OS_START"`)

* `CONTAINER_START` (value: `"CONTAINER_START"`)

* `NETWORK_UP` (value: `"NETWORK_UP"`)

* `STAGING_FILES_DOWNLOAD_START` (value: `"STAGING_FILES_DOWNLOAD_START"`)

* `STAGING_FILES_DOWNLOAD_FINISH` (value: `"STAGING_FILES_DOWNLOAD_FINISH"`)

* `SDK_INSTALL_START` (value: `"SDK_INSTALL_START"`)

* `SDK_INSTALL_FINISH` (value: `"SDK_INSTALL_FINISH"`)




