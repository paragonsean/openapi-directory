

# ValueListFilter

A list of values to filter by in ConditionalColumnSetValue

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ignoreCase** | **Boolean** | Required. Whether to ignore case when filtering by values. Defaults to false |  [optional] |
|**valuePresentList** | [**ValuePresentListEnum**](#ValuePresentListEnum) | Required. Indicates whether the filter matches rows with values that are present in the list or those with values not present in it. |  [optional] |
|**values** | **List&lt;String&gt;** | Required. The list to be used to filter by |  [optional] |



## Enum: ValuePresentListEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VALUE_PRESENT_IN_LIST_UNSPECIFIED&quot; |
| IF_VALUE_LIST | &quot;VALUE_PRESENT_IN_LIST_IF_VALUE_LIST&quot; |
| IF_VALUE_NOT_LIST | &quot;VALUE_PRESENT_IN_LIST_IF_VALUE_NOT_LIST&quot; |



