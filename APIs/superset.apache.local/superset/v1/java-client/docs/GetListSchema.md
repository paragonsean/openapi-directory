

# GetListSchema


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **List&lt;String&gt;** |  |  [optional] |
|**filters** | [**List&lt;GetListSchemaFiltersInner&gt;**](GetListSchemaFiltersInner.md) |  |  [optional] |
|**keys** | [**List&lt;KeysEnum&gt;**](#List&lt;KeysEnum&gt;) |  |  [optional] |
|**orderColumn** | **String** |  |  [optional] |
|**orderDirection** | [**OrderDirectionEnum**](#OrderDirectionEnum) |  |  [optional] |
|**page** | **Integer** |  |  [optional] |
|**pageSize** | **Integer** |  |  [optional] |



## Enum: List&lt;KeysEnum&gt;

| Name | Value |
|---- | -----|
| LIST_COLUMNS | &quot;list_columns&quot; |
| ORDER_COLUMNS | &quot;order_columns&quot; |
| LABEL_COLUMNS | &quot;label_columns&quot; |
| DESCRIPTION_COLUMNS | &quot;description_columns&quot; |
| LIST_TITLE | &quot;list_title&quot; |
| NONE | &quot;none&quot; |



## Enum: OrderDirectionEnum

| Name | Value |
|---- | -----|
| ASC | &quot;asc&quot; |
| DESC | &quot;desc&quot; |



