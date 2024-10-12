

# Rule

Represents a rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | [**LevelEnum**](#LevelEnum) | Rule nature |  |
|**operation** | [**OperationEnum**](#OperationEnum) | Comparison between the rule and score values |  |
|**outcomeLabel** | **String** | Used on the scores that fulfil this rule |  [optional] |
|**value** | **BigDecimal** | Rule value |  |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| DANGER | &quot;danger&quot; |
| WARNING | &quot;warning&quot; |
| SUCCESS | &quot;success&quot; |
| INFO | &quot;info&quot; |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| DOUBLE_EQUAL | &quot;&#x3D;&#x3D;&quot; |
| GREATER_THAN_OR_EQUAL_TO | &quot;&gt;&#x3D;&quot; |
| GREATER_THAN | &quot;&gt;&quot; |
| LESS_THAN | &quot;&lt;&quot; |
| LESS_THAN_OR_EQUAL_TO | &quot;&lt;&#x3D;&quot; |



