

# CreateCalculatedAttributeDefinitionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The display name of the calculated attribute. |  [optional] |
|**description** | **String** | The description of the calculated attribute. |  [optional] |
|**attributeDetails** | [**CreateCalculatedAttributeDefinitionRequestAttributeDetails**](CreateCalculatedAttributeDefinitionRequestAttributeDetails.md) |  |  |
|**conditions** | [**UpdateCalculatedAttributeDefinitionRequestConditions**](UpdateCalculatedAttributeDefinitionRequestConditions.md) |  |  [optional] |
|**statistic** | [**StatisticEnum**](#StatisticEnum) | The aggregation operation to perform for the calculated attribute. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. |  [optional] |



## Enum: StatisticEnum

| Name | Value |
|---- | -----|
| FIRST_OCCURRENCE | &quot;FIRST_OCCURRENCE&quot; |
| LAST_OCCURRENCE | &quot;LAST_OCCURRENCE&quot; |
| COUNT | &quot;COUNT&quot; |
| SUM | &quot;SUM&quot; |
| MINIMUM | &quot;MINIMUM&quot; |
| MAXIMUM | &quot;MAXIMUM&quot; |
| AVERAGE | &quot;AVERAGE&quot; |
| MAX_OCCURRENCE | &quot;MAX_OCCURRENCE&quot; |



