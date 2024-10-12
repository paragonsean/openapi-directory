# BatchService.JobPreparationTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commandLine** | **String** | The command line of the Job Preparation task. | [optional] 
**constraints** | [**TaskConstraints**](TaskConstraints.md) |  | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) | A list of environment variable settings for the Job Preparation task. | [optional] 
**id** | **String** | A string that uniquely identifies the job preparation task within the job. The id can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters. | [optional] 
**rerunOnNodeRebootAfterSuccess** | **Boolean** | Whether the Batch service should rerun the Job Preparation task after a compute node reboots. Note that the Job Preparation task should still be written to be idempotent because it can be rerun if the compute node is rebooted while Job Preparation task is still running. The default value is true. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | A list of files that the Batch service will download to the compute node before running the command line. | [optional] 
**runElevated** | **Boolean** | Whether to run the Job Preparation task in elevated mode. The default value is false. | [optional] 
**waitForSuccess** | **Boolean** | Whether the Batch service should wait for the Job Preparation task to complete successfully before scheduling any other tasks of the job on the compute node. | [optional] 


