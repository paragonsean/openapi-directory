# ControlApiV1.AwsSqsRulePatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestMode** | **String** | Single request mode sends each event separately to the endpoint specified by the rule. You can read more about single request mode events in the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#batching\&quot;&gt;Ably documentation&lt;/a&gt;. | [optional] 
**ruleType** | **String** | The type of rule. In this case AWS SQS. See the &lt;a href&#x3D;\&quot;https://ably.com/integrations\&quot;&gt;documentation&lt;/a&gt; for further information. | [optional] 
**source** | [**RuleSource**](RuleSource.md) |  | [optional] 
**status** | **String** | The status of the rule. Rules can be enabled or disabled. | [optional] 
**target** | [**AwsSqsRulePatchTarget**](AwsSqsRulePatchTarget.md) |  | [optional] 



## Enum: RequestModeEnum


* `single` (value: `"single"`)





## Enum: RuleTypeEnum


* `aws/sqs` (value: `"aws/sqs"`)





## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




