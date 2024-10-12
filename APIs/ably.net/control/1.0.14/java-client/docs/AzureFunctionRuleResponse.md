

# AzureFunctionRuleResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **Object** |  |  [optional] |
|**appId** | **String** | The Ably application ID. |  [optional] |
|**created** | **BigDecimal** | Unix timestamp representing the date and time of creation of the rule. |  [optional] |
|**id** | **String** | The rule ID. |  [optional] |
|**modified** | **BigDecimal** | Unix timestamp representing the date and time of last modification of the rule. |  [optional] |
|**requestMode** | [**RequestModeEnum**](#RequestModeEnum) | This is Single Request mode or Batch Request mode. Single Request mode sends each event separately to the endpoint specified by the rule. Batch Request mode rolls up multiple events into the same request. You can read more about the difference between single and batched events in the Ably &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#batching\&quot;&gt;documentation&lt;/a&gt;. |  |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | The type of rule. In this case Microsoft Azure Function. See the &lt;a href&#x3D;\&quot;https://ably.com/integrations\&quot;&gt;documentation&lt;/a&gt; for further information. |  |
|**source** | [**RuleSource**](RuleSource.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the rule. Rules can be enabled or disabled. |  [optional] |
|**target** | [**AzureFunctionRulePostTarget**](AzureFunctionRulePostTarget.md) |  |  |
|**version** | **String** | API version. Events and the format of their payloads are versioned. Please see the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events\&quot;&gt;Events documentation&lt;/a&gt;. |  [optional] |



## Enum: RequestModeEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |
| BATCH | &quot;batch&quot; |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| HTTP_AZURE_FUNCTION | &quot;http/azure-function&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



