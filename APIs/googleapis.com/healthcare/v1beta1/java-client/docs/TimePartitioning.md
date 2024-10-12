

# TimePartitioning

Configuration for FHIR BigQuery time-partitioned tables.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationMs** | **String** | Number of milliseconds for which to keep the storage for a partition. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of partitioning. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PARTITION_TYPE_UNSPECIFIED | &quot;PARTITION_TYPE_UNSPECIFIED&quot; |
| HOUR | &quot;HOUR&quot; |
| DAY | &quot;DAY&quot; |
| MONTH | &quot;MONTH&quot; |
| YEAR | &quot;YEAR&quot; |



