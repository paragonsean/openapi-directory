

# MultiInstanceSettings

Settings which specify how to run a multi-instance task. Multi-instance tasks are commonly used to support MPI tasks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonResourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | A list of files that the Batch service will download before running the coordination command line. The difference between common resource files and task resource files is that common resource files are downloaded for all subtasks including the primary, whereas task resource files are downloaded only for the primary. |  [optional] |
|**coordinationCommandLine** | **String** | The command to run on the compute node instances for coordinating among the subtasks. |  [optional] |
|**numberOfInstances** | **Integer** | The number of compute nodes required by the multi-instance task. |  |



