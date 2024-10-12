# TheJiraCloudPlatformRestApi.Workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | The creation date of the workflow. | [optional] 
**description** | **String** | The description of the workflow. | 
**hasDraftWorkflow** | **Boolean** | Whether the workflow has a draft version. | [optional] 
**id** | [**PublishedWorkflowId**](PublishedWorkflowId.md) |  | 
**isDefault** | **Boolean** | Whether this is the default workflow. | [optional] 
**operations** | [**WorkflowOperations**](WorkflowOperations.md) |  | [optional] 
**projects** | [**[ProjectDetails]**](ProjectDetails.md) | The projects the workflow is assigned to, through workflow schemes. | [optional] 
**schemes** | [**[WorkflowSchemeIdName]**](WorkflowSchemeIdName.md) | The workflow schemes the workflow is assigned to. | [optional] 
**statuses** | [**[WorkflowStatus]**](WorkflowStatus.md) | The statuses of the workflow. | [optional] 
**transitions** | [**[Transition]**](Transition.md) | The transitions of the workflow. | [optional] 
**updated** | **Date** | The last edited date of the workflow. | [optional] 


