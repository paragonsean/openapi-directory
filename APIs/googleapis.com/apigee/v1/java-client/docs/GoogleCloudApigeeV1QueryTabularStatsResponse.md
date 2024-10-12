

# GoogleCloudApigeeV1QueryTabularStatsResponse

Encapsulates two kinds of stats that are results of the dimensions and aggregations requested. - Tabular rows. - Time series data. Example of tabular rows, Represents security stats results as a row of flat values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **List&lt;String&gt;** | Column names corresponding to the same order as the inner values in the stats field. |  [optional] |
|**nextPageToken** | **String** | Next page token. |  [optional] |
|**values** | **List&lt;List&lt;Object&gt;&gt;** | Resultant rows from the executed query. |  [optional] |



