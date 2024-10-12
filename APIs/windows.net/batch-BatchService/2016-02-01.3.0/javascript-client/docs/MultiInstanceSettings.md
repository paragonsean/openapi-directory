# BatchService.MultiInstanceSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonResourceFiles** | [**[ResourceFile]**](ResourceFile.md) | A list of files that the Batch service will download before running the coordination command line. The difference between common resource files and task resource files is that common resource files are downloaded for all subtasks including the primary, whereas task resource files are downloaded only for the primary. | [optional] 
**coordinationCommandLine** | **String** | The command to run on the compute node instances for coordinating among the subtasks. | [optional] 
**numberOfInstances** | **Number** | The number of compute nodes required by the multi-instance task. | 


