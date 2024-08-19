

# ContainerInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bluemixApp** | **String** | The name of the Cloud Foundry app that was bound to the container during creation. |  [optional] |
|**bluemixServices** | **String** | The name of the Bluemix service instance that was bound to the container during creation. |  [optional] |
|**config** | [**ContainerConfig**](ContainerConfig.md) |  |  [optional] |
|**containerState** | **String** | The current status of the container. This state can either be transient, such as BUILDING or NETWORKING, or non-transient, such as RUNNING, SHUTDOWN, CRASHED, or SUSPENDED. |  [optional] |
|**created** | **OffsetDateTime** | The date and time the container was created. |  [optional] |
|**group** | [**Group**](Group.md) |  |  [optional] |
|**hostConfig** | [**HostConfig**](HostConfig.md) |  |  [optional] |
|**hostId** | **String** | The ID representing the physical compute host. |  [optional] |
|**humanId** | **String** | The name of the container.  |  [optional] |
|**id** | **String** | Unique identifier representing a container. |  [optional] |
|**image** | **String** | Unique identifier representing a container image. |  [optional] |
|**mounts** | **List&lt;String&gt;** | A list of volumes that are mounted to the container. |  [optional] |
|**name** | **String** | The name of the container. |  [optional] |
|**networkSettings** | [**NetworkSetting**](NetworkSetting.md) |  |  [optional] |
|**path** | **String** | The environment variable indicating the binary location. |  [optional] |
|**resolveConfPath** | **String** | Path to the resolve.conf file inside the container. The resolve.conf file is used to resolve the DNS servers. |  [optional] |
|**state** | [**ContainerState**](ContainerState.md) |  |  [optional] |
|**volumes** | [**Volume**](Volume.md) |  |  [optional] |
|**volumesRW** | **List&lt;String&gt;** | LIst of volumes that is mounted to the container. |  [optional] |



