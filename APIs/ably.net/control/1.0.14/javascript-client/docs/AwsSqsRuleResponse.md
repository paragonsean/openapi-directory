# ControlApiV1.AwsSqsRuleResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **Object** |  | [optional] 
**appId** | **String** | The Ably application ID. | [optional] 
**created** | **Number** | Unix timestamp representing the date and time of creation of the rule. | [optional] 
**id** | **String** | The rule ID. | [optional] 
**modified** | **Number** | Unix timestamp representing the date and time of last modification of the rule. | [optional] 
**requestMode** | **String** | Single request mode sends each event separately to the endpoint specified by the rule. You can read more about single request mode events in the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#batching\&quot;&gt;Ably documentation&lt;/a&gt;. | 
**ruleType** | **String** | The type of rule. In this case AWS SQS. See the &lt;a href&#x3D;\&quot;https://ably.com/integrations\&quot;&gt;documentation&lt;/a&gt; for further information. | 
**source** | [**RuleSource**](RuleSource.md) |  | 
**status** | **String** | The status of the rule. Rules can be enabled or disabled. | [optional] 
**target** | [**AwsSqsRuleResponseTarget**](AwsSqsRuleResponseTarget.md) |  | 
**version** | **String** | API version. Events and the format of their payloads are versioned. Please see the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events\&quot;&gt;Events documentation&lt;/a&gt;. | [optional] 



## Enum: RequestModeEnum


* `single` (value: `"single"`)





## Enum: RuleTypeEnum


* `aws/sqs` (value: `"aws/sqs"`)





## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




