

# MaterializedView

A materialized view considered for a query job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chosen** | **Boolean** | Whether the materialized view is chosen for the query. A materialized view can be chosen to rewrite multiple parts of the same query. If a materialized view is chosen to rewrite any part of the query, then this field is true, even if the materialized view was not chosen to rewrite others parts. |  [optional] |
|**estimatedBytesSaved** | **String** | If present, specifies a best-effort estimation of the bytes saved by using the materialized view rather than its base tables. |  [optional] |
|**rejectedReason** | [**RejectedReasonEnum**](#RejectedReasonEnum) | If present, specifies the reason why the materialized view was not chosen for the query. |  [optional] |
|**tableReference** | [**TableReference**](TableReference.md) |  |  [optional] |



## Enum: RejectedReasonEnum

| Name | Value |
|---- | -----|
| REJECTED_REASON_UNSPECIFIED | &quot;REJECTED_REASON_UNSPECIFIED&quot; |
| NO_DATA | &quot;NO_DATA&quot; |
| COST | &quot;COST&quot; |
| BASE_TABLE_TRUNCATED | &quot;BASE_TABLE_TRUNCATED&quot; |
| BASE_TABLE_DATA_CHANGE | &quot;BASE_TABLE_DATA_CHANGE&quot; |
| BASE_TABLE_PARTITION_EXPIRATION_CHANGE | &quot;BASE_TABLE_PARTITION_EXPIRATION_CHANGE&quot; |
| BASE_TABLE_EXPIRED_PARTITION | &quot;BASE_TABLE_EXPIRED_PARTITION&quot; |
| BASE_TABLE_INCOMPATIBLE_METADATA_CHANGE | &quot;BASE_TABLE_INCOMPATIBLE_METADATA_CHANGE&quot; |
| TIME_ZONE | &quot;TIME_ZONE&quot; |
| OUT_OF_TIME_TRAVEL_WINDOW | &quot;OUT_OF_TIME_TRAVEL_WINDOW&quot; |
| BASE_TABLE_FINE_GRAINED_SECURITY_POLICY | &quot;BASE_TABLE_FINE_GRAINED_SECURITY_POLICY&quot; |
| BASE_TABLE_TOO_STALE | &quot;BASE_TABLE_TOO_STALE&quot; |



