# ControlApiV1.HttpRulePost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestMode** | **String** | This is Single Request mode or Batch Request mode. Single Request mode sends each event separately to the endpoint specified by the rule. Batch Request mode rolls up multiple events into the same request. You can read more about the difference between single and batched events in the Ably &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#batching\&quot;&gt;documentation&lt;/a&gt;. | 
**ruleType** | **String** | The type of rule. See the &lt;a href&#x3D;\&quot;https://ably.com/integrations\&quot;&gt;documentation&lt;/a&gt; for further information. | 
**source** | [**RuleSource**](RuleSource.md) |  | 
**status** | **String** | The status of the rule. Rules can be enabled or disabled. | [optional] 
**target** | [**HttpRulePostTarget**](HttpRulePostTarget.md) |  | 



## Enum: RequestModeEnum


* `single` (value: `"single"`)

* `batch` (value: `"batch"`)





## Enum: RuleTypeEnum


* `http` (value: `"http"`)





## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




