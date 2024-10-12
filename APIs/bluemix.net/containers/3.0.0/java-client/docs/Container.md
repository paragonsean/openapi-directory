

# Container


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**command** | **String** | The command and arguments that were passed to the container during container creation. This command is executed when the container is started. |  [optional] |
|**containerState** | **String** | The current status of the container. The status can either be a transient state, such as BUILDING, and NETWORKING or a non-transient state, such as RUNNING, SHUTDOWN, CRASHED, PAUSED, or SUSPENDED.  |  [optional] |
|**created** | **Float** | The time when the container was created. |  [optional] |
|**env** | **List&lt;String&gt;** | A list of all the environment variables of the container. |  [optional] |
|**group** | [**Group**](Group.md) |  |  [optional] |
|**id** | **String** | Unique identifier representing a container. |  [optional] |
|**image** | **String** | Full path to the container image in your private Bluemix registry. |  [optional] |
|**imageId** | **String** | Unique identifier representing a container image. |  [optional] |
|**labels** | **Object** | List of custom metadata that was added to the container. Labels serve a wide range of uses, such as adding notes to a container. Every label is a key/ value pair. |  [optional] |
|**memory** | **Integer** | The amount of container memory in Megabyte that was assigned to your container. The memory is counted towards the quota that is allocated for the space. |  [optional] |
|**name** | **String** | The name of the container.  |  [optional] |
|**names** | **List&lt;String&gt;** | The name of the container. |  [optional] |
|**networkSettings** | [**NetworkSetting**](NetworkSetting.md) |  |  [optional] |
|**ports** | [**Port**](Port.md) |  |  [optional] |
|**sizeRootFs** | **Integer** | Total size of all the files in the container, in bytes.  |  [optional] |
|**sizeRw** | **Integer** | The size of the files which have been created or changed, if you compare the container to its base image. Just after creation, this should be zero. Ass you modify (or create) files, this size will increase. |  [optional] |
|**started** | **Float** | Time when the container was started. |  [optional] |
|**status** | **String** | The current status of the container. The status can either be a transient state, such as BUILDING, and NETWORKING or a non-transient state, such as RUNNING, SHUTDOWN, CRASHED, PAUSED, or SUSPENDED |  [optional] |
|**VCPU** | **Integer** | Number of virtual CPUs that are assigned to the container. |  [optional] |



