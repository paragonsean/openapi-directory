

# Field


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attrs** | [**List&lt;AttrsEnum&gt;**](#List&lt;AttrsEnum&gt;) | A set of attributes to extract from a Field. Find more information about attributes |  |
|**details** | [**Parserequest**](Parserequest.md) | Details themself represent independent Parse request that extracts data from linked pages. |  [optional] |
|**filters** | [**List&lt;FieldFiltersInner&gt;**](FieldFiltersInner.md) | Filters are used to pre-processing of text data when extracting. |  [optional] |
|**name** | **String** | Field name is used to aggregate results. |  |
|**selector** | **String** | Selector represents a CSS selector for data extraction within the given block. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Selector type. ( 0 - image, 1 - text, 2 - link) |  |



## Enum: List&lt;AttrsEnum&gt;

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| HREF | &quot;href&quot; |
| SRC | &quot;src&quot; |
| ALT | &quot;alt&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



