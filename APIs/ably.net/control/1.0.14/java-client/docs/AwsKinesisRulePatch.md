

# AwsKinesisRulePatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestMode** | [**RequestModeEnum**](#RequestModeEnum) | Single request mode sends each event separately to the endpoint specified by the rule. You can read more about single request mode events in the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#batching\&quot;&gt;Ably documentation&lt;/a&gt;. |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | The type of rule. In this case AWS Kinesis. See the &lt;a href&#x3D;\&quot;https://ably.com/integrations\&quot;&gt;documentation&lt;/a&gt; for further information. |  [optional] |
|**source** | [**RuleSource**](RuleSource.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the rule. Rules can be enabled or disabled. |  [optional] |
|**target** | [**AwsKinesisRulePatchTarget**](AwsKinesisRulePatchTarget.md) |  |  [optional] |



## Enum: RequestModeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| AWS_KINESIS | &quot;aws/kinesis&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



