

# GoogleCloudDatacatalogV1beta1ColumnSchema

Representation of a column within a schema. Columns could be nested inside other columns.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**column** | **String** | Required. Name of the column. |  [optional] |
|**description** | **String** | Optional. Description of the column. Default value is an empty string. |  [optional] |
|**mode** | **String** | Optional. A column&#39;s mode indicates whether the values in this column are required, nullable, etc. Only &#x60;NULLABLE&#x60;, &#x60;REQUIRED&#x60; and &#x60;REPEATED&#x60; are supported. Default mode is &#x60;NULLABLE&#x60;. |  [optional] |
|**subcolumns** | [**List&lt;GoogleCloudDatacatalogV1beta1ColumnSchema&gt;**](GoogleCloudDatacatalogV1beta1ColumnSchema.md) | Optional. Schema of sub-columns. A column can have zero or more sub-columns. |  [optional] |
|**type** | **String** | Required. Type of the column. |  [optional] |



