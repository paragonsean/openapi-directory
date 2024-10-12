# AmazonConnectService.UpdateTaskTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the task template. | [optional] 
**description** | **String** | The description of the task template. | [optional] 
**contactFlowId** | **String** | The identifier of the flow that runs by default when a task is created by referencing this template. | [optional] 
**constraints** | [**CreateTaskTemplateRequestConstraints**](CreateTaskTemplateRequestConstraints.md) |  | [optional] 
**defaults** | [**CreateTaskTemplateRequestDefaults**](CreateTaskTemplateRequestDefaults.md) |  | [optional] 
**status** | **String** | Marks a template as &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;INACTIVE&lt;/code&gt; for a task to refer to it. Tasks can only be created from &lt;code&gt;ACTIVE&lt;/code&gt; templates. If a template is marked as &lt;code&gt;INACTIVE&lt;/code&gt;, then a task that refers to this template cannot be created. | [optional] 
**fields** | [**[TaskTemplateField]**](TaskTemplateField.md) | Fields that are part of the template. | [optional] 



## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)




