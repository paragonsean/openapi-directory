# CloudRunAdminApi.JobSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeDeadlineSeconds** | **String** | Optional. Not supported. Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it. If set to zero, the system will never attempt to terminate the job based on time. Otherwise, the value must be positive integer. +optional | [optional] 
**backoffLimit** | **Number** | Optional. Specifies the number of retries per instance, before marking this job failed. If set to zero, instances will never retry on failure. +optional | [optional] 
**completions** | **Number** | Optional. Specifies the desired number of successfully finished instances the job should be run with. Setting to 1 means that parallelism is limited to 1 and the success of that instance signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ +optional | [optional] 
**parallelism** | **Number** | Optional. Specifies the maximum desired number of instances the job should run at any given time. Must be &lt;&#x3D; completions. The actual number of instances running in steady state will be less than this number when ((.spec.completions - .status.successful) &lt; .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ +optional | [optional] 
**template** | [**InstanceTemplateSpec**](InstanceTemplateSpec.md) |  | [optional] 
**ttlSecondsAfterFinished** | **Number** | Optional. Not supported. ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is set to zero, the Job won&#39;t be automatically deleted. +optional | [optional] 


