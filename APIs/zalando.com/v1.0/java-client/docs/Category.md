

# Category

Zalando API Category Schema

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childKeys** | **List&lt;String&gt;** | The list of keys of the child categories |  |
|**cid** | **Integer** | The numeric ID for a category. |  [optional] |
|**hidden** | **Boolean** | The category is hidden and not shown on the Zalando web shop |  [optional] |
|**key** | **String** | The unique key for a category |  |
|**name** | **String** | Name of the category |  |
|**outlet** | **Boolean** | Containing articles are from last seasons |  [optional] |
|**parentKey** | **String** | The key of the parent category |  [optional] |
|**suggestedFilters** | **List&lt;String&gt;** | list of filter names that are reasonable to use within this category |  |
|**targetGroup** | [**TargetGroupEnum**](#TargetGroupEnum) | The target group of the articles from this category |  |
|**type** | **String** | The type of the category. |  [optional] |



## Enum: TargetGroupEnum

| Name | Value |
|---- | -----|
| ALL | &quot;ALL&quot; |
| WOMEN | &quot;WOMEN&quot; |
| MEN | &quot;MEN&quot; |
| KIDS | &quot;KIDS&quot; |



