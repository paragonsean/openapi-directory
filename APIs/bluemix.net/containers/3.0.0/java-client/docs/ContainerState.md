

# ContainerState


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exitCode** | **String** | The exit code indicating the root cause of why the container exited. Review the Docker API documentation to find a list of exit codes and their meaning.  |  [optional] |
|**finishedAt** | **String** | Time when the container stopped. |  [optional] |
|**ghost** | **String** | Not supported by IBM Containers, empty string |  [optional] |
|**pid** | **Integer** | The process ID on the compute host that runs the container process. |  [optional] |
|**running** | **Boolean** | If set to true, the container is in a RUNNING state. If set to false, the container has stopped or crashed.  |  [optional] |
|**startedAt** | **String** | Time when the container started. |  [optional] |
|**status** | **String** | The current status of the container. This state can either be transient, such as BUILDING or NETWORKING, or non-transient, such as RUNNING, SHUTDOWN, CRASHED, or SUSPENDED. |  [optional] |



