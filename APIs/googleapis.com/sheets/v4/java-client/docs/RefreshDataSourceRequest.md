

# RefreshDataSourceRequest

Refreshes one or multiple data source objects in the spreadsheet by the specified references. The request requires an additional `bigquery.readonly` OAuth scope. If there are multiple refresh requests referencing the same data source objects in one batch, only the last refresh request is processed, and all those requests will have the same response accordingly.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceId** | **String** | Reference to a DataSource. If specified, refreshes all associated data source objects for the data source. |  [optional] |
|**force** | **Boolean** | Refreshes the data source objects regardless of the current state. If not set and a referenced data source object was in error state, the refresh will fail immediately. |  [optional] |
|**isAll** | **Boolean** | Refreshes all existing data source objects in the spreadsheet. |  [optional] |
|**references** | [**DataSourceObjectReferences**](DataSourceObjectReferences.md) |  |  [optional] |



