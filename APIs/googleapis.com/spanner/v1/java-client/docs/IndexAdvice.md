

# IndexAdvice

Recommendation to add new indexes to run queries more efficiently.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ddl** | **List&lt;String&gt;** | Optional. DDL statements to add new indexes that will improve the query. |  [optional] |
|**improvementFactor** | **Double** | Optional. Estimated latency improvement factor. For example if the query currently takes 500 ms to run and the estimated latency with new indexes is 100 ms this field will be 5. |  [optional] |



