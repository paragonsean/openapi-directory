# CloudRunAdminApi.JobStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Number** | Optional. The number of actively running instances. +optional | [optional] 
**completionTime** | **String** | Optional. Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. +optional | [optional] 
**conditions** | [**[JobCondition]**](JobCondition.md) | Optional. The latest available observations of a job&#39;s current state. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ +optional | [optional] 
**failed** | **Number** | Optional. The number of instances which reached phase Failed. +optional | [optional] 
**imageDigest** | **String** | Optional. ImageDigest holds the resolved digest for the image specified within .Spec.Template.Spec.Container.Image. The digest is resolved during the creation of the Job. This field holds the digest value regardless of whether a tag or digest was originally specified in the Container object. | [optional] 
**instances** | [**[InstanceStatus]**](InstanceStatus.md) | Optional. Status of completed, failed, and running instances. +optional | [optional] 
**observedGeneration** | **Number** | Optional. The &#39;generation&#39; of the job that was last processed by the controller. | [optional] 
**startTime** | **String** | Optional. Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. +optional | [optional] 
**succeeded** | **Number** | Optional. The number of instances which reached phase Succeeded. +optional | [optional] 


