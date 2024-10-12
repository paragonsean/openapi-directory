

# QueryResult

Execution results of the query. The result is formatted as rows represented by BigQuery compatible [schema]. When pagination is necessary, it will contains the page token to retrieve the results of following pages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Token to retrieve the next page of the results. |  [optional] |
|**rows** | **List&lt;Map&lt;String, Object&gt;&gt;** | Each row hold a query result in the format of &#x60;Struct&#x60;. |  [optional] |
|**schema** | [**TableSchema**](TableSchema.md) |  |  [optional] |
|**totalRows** | **String** | Total rows of the whole query results. |  [optional] |



