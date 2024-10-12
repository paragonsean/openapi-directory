# AwsIoTJobsDataPlane.UpdateJobExecutionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **String** | The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update. | 
**statusDetails** | **{String: String}** |  Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged. | [optional] 
**stepTimeoutInMinutes** | **Number** | Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by again calling &lt;code&gt;UpdateJobExecution&lt;/code&gt;, setting the status to &lt;code&gt;IN_PROGRESS&lt;/code&gt; and specifying a new timeout value in this field) the job execution status will be automatically set to &lt;code&gt;TIMED_OUT&lt;/code&gt;. Note that setting or resetting this timeout has no effect on that job execution timeout which may have been specified when the job was created (&lt;code&gt;CreateJob&lt;/code&gt; using field &lt;code&gt;timeoutConfig&lt;/code&gt;). | [optional] 
**expectedVersion** | **Number** | Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.) | [optional] 
**includeJobExecutionState** | **Boolean** | Optional. When included and set to true, the response contains the JobExecutionState data. The default is false. | [optional] 
**includeJobDocument** | **Boolean** | Optional. When set to true, the response contains the job document. The default is false. | [optional] 
**executionNumber** | **Number** | Optional. A number that identifies a particular job execution on a particular device. | [optional] 



## Enum: StatusEnum


* `QUEUED` (value: `"QUEUED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `TIMED_OUT` (value: `"TIMED_OUT"`)

* `REJECTED` (value: `"REJECTED"`)

* `REMOVED` (value: `"REMOVED"`)

* `CANCELED` (value: `"CANCELED"`)




