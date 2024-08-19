

# CreateRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | A unique name for the rule. |  |
|**triggerEventSource** | [**CreateRuleRequestTriggerEventSource**](CreateRuleRequestTriggerEventSource.md) |  |  |
|**function** | **String** | The conditions of the rule. |  |
|**actions** | [**List&lt;RuleAction&gt;**](RuleAction.md) | A list of actions to be run when the rule is triggered. |  |
|**publishStatus** | [**PublishStatusEnum**](#PublishStatusEnum) | The publish status of the rule. |  |
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. |  [optional] |



## Enum: PublishStatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| PUBLISHED | &quot;PUBLISHED&quot; |



