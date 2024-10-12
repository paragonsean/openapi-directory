

# WorkerShutdownNotice

Shutdown notification from workers. This is to be sent by the shutdown script of the worker VM so that the backend knows that the VM is being shut down.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | **String** | The reason for the worker shutdown. Current possible values are: \&quot;UNKNOWN\&quot;: shutdown reason is unknown. \&quot;PREEMPTION\&quot;: shutdown reason is preemption. Other possible reasons may be added in the future. |  [optional] |



