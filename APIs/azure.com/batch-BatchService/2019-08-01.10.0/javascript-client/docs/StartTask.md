# BatchService.StartTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commandLine** | **String** | The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using \&quot;cmd /c MyCommand\&quot; in Windows or \&quot;/bin/sh -c MyCommand\&quot; in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables). | 
**containerSettings** | [**TaskContainerSettings**](TaskContainerSettings.md) |  | [optional] 
**environmentSettings** | [**[EnvironmentSetting]**](EnvironmentSetting.md) |  | [optional] 
**maxTaskRetryCount** | **Number** | The Batch service retries a Task if its exit code is nonzero. Note that this value specifically controls the number of retries. The Batch service will try the Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries the Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry the Task. If the maximum retry count is -1, the Batch service retries the Task without limit. | [optional] 
**resourceFiles** | [**[ResourceFile]**](ResourceFile.md) | Files listed under this element are located in the Task&#39;s working directory. | [optional] 
**userIdentity** | [**UserIdentity**](UserIdentity.md) |  | [optional] 
**waitForSuccess** | **Boolean** | If true and the StartTask fails on a Node, the Batch service retries the StartTask up to its maximum retry count (maxTaskRetryCount). If the Task has still not completed successfully after all retries, then the Batch service marks the Node unusable, and will not schedule Tasks to it. This condition can be detected via the Compute Node state and failure info details. If false, the Batch service will not wait for the StartTask to complete. In this case, other Tasks can start executing on the Compute Node while the StartTask is still running; and even if the StartTask fails, new Tasks will continue to be scheduled on the Compute Node. The default is true. | [optional] 


