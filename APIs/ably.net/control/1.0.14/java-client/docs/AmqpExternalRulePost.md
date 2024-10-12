

# AmqpExternalRulePost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestMode** | [**RequestModeEnum**](#RequestModeEnum) | Single request mode sends each event separately to the endpoint specified by the rule. You can read more about single request mode events in the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#batching\&quot;&gt;Ably documentation&lt;/a&gt;. |  |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | The type of rule. In this case AMQP external (using Firehose). See the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/firehose\&quot;&gt;documentation&lt;/a&gt; for further information. |  |
|**source** | [**RuleSource**](RuleSource.md) |  |  |
|**target** | [**AmqpExternalRulePostTarget**](AmqpExternalRulePostTarget.md) |  |  |



## Enum: RequestModeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| AMQP_EXTERNAL | &quot;amqp/external&quot; |



