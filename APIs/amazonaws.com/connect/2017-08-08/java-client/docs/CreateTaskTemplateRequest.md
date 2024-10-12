

# CreateTaskTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the task template. |  |
|**description** | **String** | The description of the task template. |  [optional] |
|**contactFlowId** | **String** | The identifier of the flow that runs by default when a task is created by referencing this template. |  [optional] |
|**constraints** | [**CreateTaskTemplateRequestConstraints**](CreateTaskTemplateRequestConstraints.md) |  |  [optional] |
|**defaults** | [**CreateTaskTemplateRequestDefaults**](CreateTaskTemplateRequestDefaults.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Marks a template as &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;INACTIVE&lt;/code&gt; for a task to refer to it. Tasks can only be created from &lt;code&gt;ACTIVE&lt;/code&gt; templates. If a template is marked as &lt;code&gt;INACTIVE&lt;/code&gt;, then a task that refers to this template cannot be created.  |  [optional] |
|**fields** | [**List&lt;TaskTemplateField&gt;**](TaskTemplateField.md) | Fields that are part of the template. |  |
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



