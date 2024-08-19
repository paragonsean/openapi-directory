

# GoogleCloudFunctionRulePost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestMode** | [**RequestModeEnum**](#RequestModeEnum) | This is Single Request mode or Batch Request mode. Single Request mode sends each event separately to the endpoint specified by the rule. Batch Request mode rolls up multiple events into the same request. You can read more about the difference between single and batched events in the Ably &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#batching\&quot;&gt;documentation&lt;/a&gt;. |  |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | The type of rule. In this case Google Cloud Function. See the &lt;a href&#x3D;\&quot;https://ably.com/integrations\&quot;&gt;documentation&lt;/a&gt; for further information. |  |
|**source** | [**RuleSource**](RuleSource.md) |  |  |
|**target** | [**GoogleCloudFunctionRulePostTarget**](GoogleCloudFunctionRulePostTarget.md) |  |  |



## Enum: RequestModeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |
| BATCH | &quot;batch&quot; |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| HTTP_GOOGLE_CLOUD_FUNCTION | &quot;http/google-cloud-function&quot; |



