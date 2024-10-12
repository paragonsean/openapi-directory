# BatchService.MultiInstanceSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonResourceFiles** | [**[ResourceFile]**](ResourceFile.md) | The difference between common resource files and task resource files is that common resource files are downloaded for all subtasks including the primary, whereas task resource files are downloaded only for the primary. Also note that these resource files are not downloaded to the task working directory, but instead are downloaded to the task root directory (one directory above the working directory). | [optional] 
**coordinationCommandLine** | **String** | A typical coordination command line launches a background service and verifies that the service is ready to process inter-node messages. | 
**numberOfInstances** | **Number** | If omitted, the default is 1. | [optional] 


