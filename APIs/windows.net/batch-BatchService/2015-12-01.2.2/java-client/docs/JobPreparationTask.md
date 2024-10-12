

# JobPreparationTask

A Job Preparation task to run before any tasks of the job on any given compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commandLine** | **String** | Gets or sets the command line of the Job Preparation task. |  [optional] |
|**constraints** | [**TaskConstraints**](TaskConstraints.md) |  |  [optional] |
|**environmentSettings** | [**List&lt;EnvironmentSetting&gt;**](EnvironmentSetting.md) | Gets or sets a list of environment variable settings for the Job Preparation task. |  [optional] |
|**id** | **String** | Gets or sets a string that uniquely identifies the job preparation task within the job. The id can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters. |  [optional] |
|**rerunOnNodeRebootAfterSuccess** | **Boolean** | Gets or sets whether the Batch service should rerun the Job Preparation task after a compute node reboots. The default value is true. |  [optional] |
|**resourceFiles** | [**List&lt;ResourceFile&gt;**](ResourceFile.md) | Gets or sets a list of files that Batch will download to the compute node before running the command line. |  [optional] |
|**runElevated** | **Boolean** | Gets or sets whether to run the Job Preparation task in elevated mode. The default value is false. |  [optional] |
|**waitForSuccess** | **Boolean** | Gets or sets whether the Batch Service should wait for the Job Preparation task to complete successfully before scheduling any other tasks of the job on the compute node. |  [optional] |



