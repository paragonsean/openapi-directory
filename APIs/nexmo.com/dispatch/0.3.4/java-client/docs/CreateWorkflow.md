

# CreateWorkflow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**template** | [**TemplateEnum**](#TemplateEnum) | The template that the Dispatch API will execute. For the initial version of the API the only available value will be failover |  [optional] |
|**workflow** | [**List&lt;CreateWorkflowWorkflowInner&gt;**](CreateWorkflowWorkflowInner.md) | Contains a message object that must reflect the current /messages resource. All parameters within the content object reflect the /messages docs. |  [optional] |



## Enum: TemplateEnum

| Name | Value |
|---- | -----|
| FAILOVER | &quot;failover&quot; |



