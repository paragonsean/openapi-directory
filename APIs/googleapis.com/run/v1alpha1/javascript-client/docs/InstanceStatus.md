# CloudRunAdminApi.InstanceStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completionTime** | **String** | Optional. Represents time when the instance was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. +optional | [optional] 
**failed** | **Number** | Optional. The number of times this instance exited with code &gt; 0; +optional | [optional] 
**index** | **Number** | Required. Index of the instance, unique per Job, and beginning at 0. | [optional] 
**lastAttemptResult** | [**InstanceAttemptResult**](InstanceAttemptResult.md) |  | [optional] 
**lastExitCode** | **Number** | Optional. Last exit code seen for this instance. +optional | [optional] 
**restarted** | **Number** | Optional. The number of times this instance was restarted. Instances are restarted according the restartPolicy configured in the Job template. +optional | [optional] 
**startTime** | **String** | Optional. Represents time when the instance was created by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. +optional | [optional] 
**succeeded** | **Number** | Optional. The number of times this instance exited with code &#x3D;&#x3D; 0. +optional | [optional] 


