

# BigQueryDataSourceSpec

The specification of a BigQuery data source that's connected to a sheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectId** | **String** | The ID of a BigQuery enabled Google Cloud project with a billing account attached. For any queries executed against the data source, the project is charged. |  [optional] |
|**querySpec** | [**BigQueryQuerySpec**](BigQueryQuerySpec.md) |  |  [optional] |
|**tableSpec** | [**BigQueryTableSpec**](BigQueryTableSpec.md) |  |  [optional] |



