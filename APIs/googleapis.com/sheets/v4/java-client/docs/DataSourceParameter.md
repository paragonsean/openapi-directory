

# DataSourceParameter

A parameter in a data source's query. The parameter allows the user to pass in values from the spreadsheet into a query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Named parameter. Must be a legitimate identifier for the DataSource that supports it. For example, [BigQuery identifier](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#identifiers). |  [optional] |
|**namedRangeId** | **String** | ID of a NamedRange. Its size must be 1x1. |  [optional] |
|**range** | [**GridRange**](GridRange.md) |  |  [optional] |



