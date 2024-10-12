

# RuleAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | The Ably application ID. |  [optional] |
|**created** | **BigDecimal** | Unix timestamp representing the date and time of creation of the rule. |  [optional] |
|**id** | **String** | The rule ID. |  [optional] |
|**modified** | **BigDecimal** | Unix timestamp representing the date and time of last modification of the rule. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the rule. Rules can be enabled or disabled. |  [optional] |
|**version** | **String** | API version. Events and the format of their payloads are versioned. Please see the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events\&quot;&gt;Events documentation&lt;/a&gt;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



