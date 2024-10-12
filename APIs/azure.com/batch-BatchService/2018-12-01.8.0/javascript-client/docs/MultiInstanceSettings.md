# BatchService.MultiInstanceSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonResourceFiles** | [**[ResourceFile]**](ResourceFile.md) | The difference between common resource files and task resource files is that common resource files are downloaded for all subtasks including the primary, whereas task resource files are downloaded only for the primary. Also note that these resource files are not downloaded to the task working directory, but instead are downloaded to the task root directory (one directory above the working directory).  There is a maximum size for the list of resource files.  When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers. | [optional] 
**coordinationCommandLine** | **String** | A typical coordination command line launches a background service and verifies that the service is ready to process inter-node messages. | 
**numberOfInstances** | **Number** | If omitted, the default is 1. | [optional] 


