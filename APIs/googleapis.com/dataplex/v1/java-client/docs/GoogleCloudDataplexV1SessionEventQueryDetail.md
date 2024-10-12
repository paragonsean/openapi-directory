

# GoogleCloudDataplexV1SessionEventQueryDetail

Execution details of the query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataProcessedBytes** | **String** | The data processed by the query. |  [optional] |
|**duration** | **String** | Time taken for execution of the query. |  [optional] |
|**engine** | [**EngineEnum**](#EngineEnum) | Query Execution engine. |  [optional] |
|**queryId** | **String** | The unique Query id identifying the query. |  [optional] |
|**queryText** | **String** | The query text executed. |  [optional] |
|**resultSizeBytes** | **String** | The size of results the query produced. |  [optional] |



## Enum: EngineEnum

| Name | Value |
|---- | -----|
| ENGINE_UNSPECIFIED | &quot;ENGINE_UNSPECIFIED&quot; |
| SPARK_SQL | &quot;SPARK_SQL&quot; |
| BIGQUERY | &quot;BIGQUERY&quot; |



