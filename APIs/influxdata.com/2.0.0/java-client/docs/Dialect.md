

# Dialect

Dialect are options to change the default CSV output format; https://www.w3.org/TR/2015/REC-tabular-metadata-20151217/#dialect-descriptions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | [**Set&lt;AnnotationsEnum&gt;**](#Set&lt;AnnotationsEnum&gt;) | https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/#columns |  [optional] |
|**commentPrefix** | **String** | Character prefixed to comment strings |  [optional] |
|**dateTimeFormat** | [**DateTimeFormatEnum**](#DateTimeFormatEnum) | Format of timestamps |  [optional] |
|**delimiter** | **String** | Separator between cells; the default is , |  [optional] |
|**header** | **Boolean** | If true, the results will contain a header row |  [optional] |



## Enum: Set&lt;AnnotationsEnum&gt;

| Name | Value |
|---- | -----|
| GROUP | &quot;group&quot; |
| DATATYPE | &quot;datatype&quot; |
| DEFAULT | &quot;default&quot; |



## Enum: DateTimeFormatEnum

| Name | Value |
|---- | -----|
| RFC3339 | &quot;RFC3339&quot; |
| RFC3339_NANO | &quot;RFC3339Nano&quot; |



