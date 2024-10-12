# BatchService.JobManagerTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commandLine** | **String** | Gets or sets the command line of the Job Manager task. | [optional] 
**constraints** | [**TaskConstraints**](TaskConstraints.md) |  | [optional] 
**displayName** | **String** | Gets or sets the display name of the Job Manager task. | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) | Gets or sets a list of environment variable settings for the Job Manager task. | [optional] 
**id** | **String** | Gets or sets a string that uniquely identifies the Job Manager task. A GUID is recommended. | [optional] 
**killJobOnCompletion** | **Boolean** | Gets or sets whether completion of the Job Manager task signifies completion of the entire job. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | Gets or sets a list of files that Batch will download to the compute node before running the command line. | [optional] 
**runElevated** | **Boolean** | Gets or sets whether to run the Job Manager task in elevated mode. The default value is false. | [optional] 
**runExclusive** | **Boolean** | Gets or sets whether the Job Manager task requires exclusive use of the compute node where it runs. | [optional] 


