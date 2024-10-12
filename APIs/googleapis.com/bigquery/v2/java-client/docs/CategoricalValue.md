

# CategoricalValue

Representative value of a categorical feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryCounts** | [**List&lt;CategoryCount&gt;**](CategoryCount.md) | Counts of all categories for the categorical feature. If there are more than ten categories, we return top ten (by count) and return one more CategoryCount with category \&quot;_OTHER_\&quot; and count as aggregate counts of remaining categories. |  [optional] |



