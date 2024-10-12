

# UpdateRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the rule. You can change the name only if &lt;code&gt;TriggerEventSource&lt;/code&gt; is one of the following values: &lt;code&gt;OnZendeskTicketCreate&lt;/code&gt; | &lt;code&gt;OnZendeskTicketStatusUpdate&lt;/code&gt; | &lt;code&gt;OnSalesforceCaseCreate&lt;/code&gt;  |  |
|**function** | **String** | The conditions of the rule. |  |
|**actions** | [**List&lt;RuleAction&gt;**](RuleAction.md) | A list of actions to be run when the rule is triggered. |  |
|**publishStatus** | [**PublishStatusEnum**](#PublishStatusEnum) | The publish status of the rule. |  |



## Enum: PublishStatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| PUBLISHED | &quot;PUBLISHED&quot; |



