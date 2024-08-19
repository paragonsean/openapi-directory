# AmazonConnectService.UpdateRuleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the rule. You can change the name only if &lt;code&gt;TriggerEventSource&lt;/code&gt; is one of the following values: &lt;code&gt;OnZendeskTicketCreate&lt;/code&gt; | &lt;code&gt;OnZendeskTicketStatusUpdate&lt;/code&gt; | &lt;code&gt;OnSalesforceCaseCreate&lt;/code&gt;  | 
**_function** | **String** | The conditions of the rule. | 
**actions** | [**[RuleAction]**](RuleAction.md) | A list of actions to be run when the rule is triggered. | 
**publishStatus** | **String** | The publish status of the rule. | 



## Enum: PublishStatusEnum


* `DRAFT` (value: `"DRAFT"`)

* `PUBLISHED` (value: `"PUBLISHED"`)




