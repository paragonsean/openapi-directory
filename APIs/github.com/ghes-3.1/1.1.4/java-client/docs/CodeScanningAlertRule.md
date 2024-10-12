

# CodeScanningAlertRule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A short description of the rule used to detect the alert. |  [optional] |
|**fullDescription** | **String** | description of the rule used to detect the alert. |  [optional] |
|**help** | **String** | Detailed documentation for the rule as GitHub Flavored Markdown. |  [optional] |
|**id** | **String** | A unique identifier for the rule used to detect the alert. |  [optional] |
|**name** | **String** | The name of the rule used to detect the alert. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity of the alert. |  [optional] |
|**tags** | **List&lt;String&gt;** | A set of tags applicable for the rule. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| NOTE | &quot;note&quot; |
| WARNING | &quot;warning&quot; |
| ERROR | &quot;error&quot; |



