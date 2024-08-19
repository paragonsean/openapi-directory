# ControlApiV1.CloudflareWorkerRulePatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestMode** | **String** | This is Single Request mode or Batch Request mode. Single Request mode sends each event separately to the endpoint specified by the rule. Batch Request mode rolls up multiple events into the same request. You can read more about the difference between single and batched events in the Ably &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#batching\&quot;&gt;documentation&lt;/a&gt;. | [optional] 
**ruleType** | **String** | The type of rule. In this case Cloudflare Worker. See the &lt;a href&#x3D;\&quot;https://ably.com/integrations\&quot;&gt;documentation&lt;/a&gt; for further information. | [optional] 
**source** | [**RuleSource**](RuleSource.md) |  | [optional] 
**status** | **String** | The status of the rule. Rules can be enabled or disabled. | [optional] 
**target** | [**CloudflareWorkerRulePatchTarget**](CloudflareWorkerRulePatchTarget.md) |  | [optional] 



## Enum: RequestModeEnum


* `single` (value: `"single"`)

* `batch` (value: `"batch"`)





## Enum: RuleTypeEnum


* `http/cloudflare-worker` (value: `"http/cloudflare-worker"`)





## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




