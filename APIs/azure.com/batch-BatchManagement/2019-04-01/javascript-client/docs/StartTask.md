# BatchManagement.StartTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commandLine** | **String** | The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. Required if any other properties of the startTask are specified. | [optional] 
**containerSettings** | [**TaskContainerSettings**](TaskContainerSettings.md) |  | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) |  | [optional] 
**maxTaskRetryCount** | **Number** | The Batch service retries a task if its exit code is nonzero. Note that this value specifically controls the number of retries. The Batch service will try the task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries the task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry the task. If the maximum retry count is -1, the Batch service retries the task without limit. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) |  | [optional] 
**userIdentity** | [**UserIdentity**](UserIdentity.md) |  | [optional] 
**waitForSuccess** | **Boolean** | If true and the start task fails on a compute node, the Batch service retries the start task up to its maximum retry count (maxTaskRetryCount). If the task has still not completed successfully after all retries, then the Batch service marks the compute node unusable, and will not schedule tasks to it. This condition can be detected via the node state and scheduling error detail. If false, the Batch service will not wait for the start task to complete. In this case, other tasks can start executing on the compute node while the start task is still running; and even if the start task fails, new tasks will continue to be scheduled on the node. The default is false. | [optional] 


