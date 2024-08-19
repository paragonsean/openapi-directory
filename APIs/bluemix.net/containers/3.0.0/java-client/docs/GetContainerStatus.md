

# GetContainerStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nameOrId** | **String** | The unique identifier of the container.  |  |
|**status** | **String** | The current status of the container. The status can either be a transient one, such as BUILDING or NETWORKING, or a non-transient one, such as RUNNING, SHUTDOWN, CRASHED, or SUSPENDED.  |  [optional] |
|**_transient** | **Boolean** | When set to true, the current container state is temporary and will change soon. An example for a transient state is the BUILDING state. A container that is created will be set to the BUILDING state until all container layers are created and the container is started. When set to false, the container state is permanent, such as CRASHED. |  [optional] |



