

# Task

For details see: [airflow.models.BaseOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/index.html#airflow.models.BaseOperator) 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classRef** | [**ClassReference**](ClassReference.md) |  |  [optional] |
|**dependsOnPast** | **Boolean** |  |  [optional] [readonly] |
|**downstreamTaskIds** | **List&lt;String&gt;** |  |  [optional] [readonly] |
|**endDate** | **OffsetDateTime** |  |  [optional] [readonly] |
|**executionTimeout** | [**TimeDelta**](TimeDelta.md) |  |  [optional] |
|**extraLinks** | [**List&lt;TaskExtraLinksInner&gt;**](TaskExtraLinksInner.md) |  |  [optional] [readonly] |
|**isMapped** | **Boolean** |  |  [optional] [readonly] |
|**owner** | **String** |  |  [optional] [readonly] |
|**pool** | **String** |  |  [optional] [readonly] |
|**poolSlots** | **BigDecimal** |  |  [optional] [readonly] |
|**priorityWeight** | **BigDecimal** |  |  [optional] [readonly] |
|**queue** | **String** |  |  [optional] [readonly] |
|**retries** | **BigDecimal** |  |  [optional] [readonly] |
|**retryDelay** | [**TimeDelta**](TimeDelta.md) |  |  [optional] |
|**retryExponentialBackoff** | **Boolean** |  |  [optional] [readonly] |
|**startDate** | **OffsetDateTime** |  |  [optional] [readonly] |
|**subDag** | [**DAG**](DAG.md) |  |  [optional] |
|**taskId** | **String** |  |  [optional] [readonly] |
|**templateFields** | **List&lt;String&gt;** |  |  [optional] [readonly] |
|**triggerRule** | **TriggerRule** |  |  [optional] |
|**uiColor** | **String** | Color in hexadecimal notation. |  [optional] |
|**uiFgcolor** | **String** | Color in hexadecimal notation. |  [optional] |
|**waitForDownstream** | **Boolean** |  |  [optional] [readonly] |
|**weightRule** | **WeightRule** |  |  [optional] |



