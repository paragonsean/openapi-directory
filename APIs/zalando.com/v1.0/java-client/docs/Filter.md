

# Filter

Zalando API Filter Schema

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**multiValue** | **Boolean** | can this filter be used multiple times with different values in one search request |  |
|**name** | **String** | The unique name for a filter |  |
|**type** | [**TypeEnum**](#TypeEnum) | filter enum types |  |
|**values** | [**List&lt;FilterValue&gt;**](FilterValue.md) | only if type is &#39;enum&#39; this list contains all possible filter values |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SKU | &quot;SKU&quot; |
| KEY | &quot;KEY&quot; |
| ENUM | &quot;ENUM&quot; |
| STRING | &quot;STRING&quot; |
| RANGE | &quot;RANGE&quot; |



