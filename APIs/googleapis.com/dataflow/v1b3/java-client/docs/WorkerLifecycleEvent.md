

# WorkerLifecycleEvent

A report of an event in a worker's lifecycle. The proto contains one event, because the worker is expected to asynchronously send each message immediately after the event. Due to this asynchrony, messages may arrive out of order (or missing), and it is up to the consumer to interpret. The timestamp of the event is in the enclosing WorkerMessage proto.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerStartTime** | **String** | The start time of this container. All events will report this so that events can be grouped together across container/VM restarts. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) | The event being reported. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Other stats that can accompany an event. E.g. { \&quot;downloaded_bytes\&quot; : \&quot;123456\&quot; } |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| UNKNOWN_EVENT | &quot;UNKNOWN_EVENT&quot; |
| OS_START | &quot;OS_START&quot; |
| CONTAINER_START | &quot;CONTAINER_START&quot; |
| NETWORK_UP | &quot;NETWORK_UP&quot; |
| STAGING_FILES_DOWNLOAD_START | &quot;STAGING_FILES_DOWNLOAD_START&quot; |
| STAGING_FILES_DOWNLOAD_FINISH | &quot;STAGING_FILES_DOWNLOAD_FINISH&quot; |
| SDK_INSTALL_START | &quot;SDK_INSTALL_START&quot; |
| SDK_INSTALL_FINISH | &quot;SDK_INSTALL_FINISH&quot; |



