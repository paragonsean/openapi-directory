# CloudDataprocApi.WorkflowTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time template was created. | [optional] [readonly] 
**dagTimeout** | **String** | Optional. Timeout duration for the DAG of jobs, expressed in seconds (see JSON representation of duration (https://developers.google.com/protocol-buffers/docs/proto3#json)). The timeout duration must be from 10 minutes (\&quot;600s\&quot;) to 24 hours (\&quot;86400s\&quot;). The timer begins when the first job is submitted. If the workflow is running at the end of the timeout period, any remaining jobs are cancelled, the workflow is ended, and if the workflow was running on a managed cluster, the cluster is deleted. | [optional] 
**encryptionConfig** | [**GoogleCloudDataprocV1WorkflowTemplateEncryptionConfig**](GoogleCloudDataprocV1WorkflowTemplateEncryptionConfig.md) |  | [optional] 
**id** | **String** |  | [optional] 
**jobs** | [**[OrderedJob]**](OrderedJob.md) | Required. The Directed Acyclic Graph of Jobs to submit. | [optional] 
**labels** | **{String: String}** | Optional. The labels to associate with this template. These labels will be propagated to all jobs and clusters created by the workflow instance.Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt).Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt).No more than 32 labels can be associated with a template. | [optional] 
**name** | **String** | Output only. The resource name of the workflow template, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/regions/{region}/workflowTemplates/{template_id} For projects.locations.workflowTemplates, the resource name of the template has the following format: projects/{project_id}/locations/{location}/workflowTemplates/{template_id} | [optional] [readonly] 
**parameters** | [**[TemplateParameter]**](TemplateParameter.md) | Optional. Template parameters whose values are substituted into the template. Values for parameters must be provided when the template is instantiated. | [optional] 
**placement** | [**WorkflowTemplatePlacement**](WorkflowTemplatePlacement.md) |  | [optional] 
**updateTime** | **String** | Output only. The time template was last updated. | [optional] [readonly] 
**version** | **Number** | Optional. Used to perform a consistent read-modify-write.This field should be left blank for a CreateWorkflowTemplate request. It is required for an UpdateWorkflowTemplate request, and must match the current server version. A typical update template flow would fetch the current template with a GetWorkflowTemplate request, which will return the current template with the version field filled in with the current server version. The user updates other fields in the template, then returns it as part of the UpdateWorkflowTemplate request. | [optional] 


