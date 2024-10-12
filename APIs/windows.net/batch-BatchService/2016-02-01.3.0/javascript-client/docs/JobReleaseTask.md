# BatchService.JobReleaseTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commandLine** | **String** | The command line of the Job Release task. | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) | A list of environment variable settings for the Job Release task. | [optional] 
**id** | **String** | A string that uniquely identifies the Job Release task within the job. The id can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters. | [optional] 
**maxWallClockTime** | **String** | The maximum elapsed time that the Job Release task may run on a given compute node, measured from the time the task starts. If the task does not complete within the time limit, the Batch service terminates it. The default value is 15 minutes. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | A list of files that the Batch service will download to the compute node before running the command line. | [optional] 
**retentionTime** | **String** | The minimum time to retain the working directory for the Job Release task on the compute node. After this time, the Batch service may delete the working directory and all its contents. The default is infinite. | [optional] 
**runElevated** | **Boolean** | Whether to run the Job Release task in elevated mode. The default value is false. | [optional] 


