

# UpdateDataSourceRequest

Updates a data source. After the data source is updated successfully, an execution is triggered to refresh the associated DATA_SOURCE sheet to read data from the updated data source. The request requires an additional `bigquery.readonly` OAuth scope.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSource** | [**DataSource**](DataSource.md) |  |  [optional] |
|**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;dataSource&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. |  [optional] |



