

# StartNextPendingJobExecutionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**statusDetails** | **Map&lt;String, String&gt;** | A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged. |  [optional] |
|**stepTimeoutInMinutes** | **Integer** | Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by calling &lt;code&gt;UpdateJobExecution&lt;/code&gt;, setting the status to &lt;code&gt;IN_PROGRESS&lt;/code&gt; and specifying a new timeout value in field &lt;code&gt;stepTimeoutInMinutes&lt;/code&gt;) the job execution status will be automatically set to &lt;code&gt;TIMED_OUT&lt;/code&gt;. Note that setting this timeout has no effect on that job execution timeout which may have been specified when the job was created (&lt;code&gt;CreateJob&lt;/code&gt; using field &lt;code&gt;timeoutConfig&lt;/code&gt;). |  [optional] |



