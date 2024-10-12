# BigQueryApi.MaterializedView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chosen** | **Boolean** | Whether the materialized view is chosen for the query. A materialized view can be chosen to rewrite multiple parts of the same query. If a materialized view is chosen to rewrite any part of the query, then this field is true, even if the materialized view was not chosen to rewrite others parts. | [optional] 
**estimatedBytesSaved** | **String** | If present, specifies a best-effort estimation of the bytes saved by using the materialized view rather than its base tables. | [optional] 
**rejectedReason** | **String** | If present, specifies the reason why the materialized view was not chosen for the query. | [optional] 
**tableReference** | [**TableReference**](TableReference.md) |  | [optional] 



## Enum: RejectedReasonEnum


* `REJECTED_REASON_UNSPECIFIED` (value: `"REJECTED_REASON_UNSPECIFIED"`)

* `NO_DATA` (value: `"NO_DATA"`)

* `COST` (value: `"COST"`)

* `BASE_TABLE_TRUNCATED` (value: `"BASE_TABLE_TRUNCATED"`)

* `BASE_TABLE_DATA_CHANGE` (value: `"BASE_TABLE_DATA_CHANGE"`)

* `BASE_TABLE_PARTITION_EXPIRATION_CHANGE` (value: `"BASE_TABLE_PARTITION_EXPIRATION_CHANGE"`)

* `BASE_TABLE_EXPIRED_PARTITION` (value: `"BASE_TABLE_EXPIRED_PARTITION"`)

* `BASE_TABLE_INCOMPATIBLE_METADATA_CHANGE` (value: `"BASE_TABLE_INCOMPATIBLE_METADATA_CHANGE"`)

* `TIME_ZONE` (value: `"TIME_ZONE"`)

* `OUT_OF_TIME_TRAVEL_WINDOW` (value: `"OUT_OF_TIME_TRAVEL_WINDOW"`)

* `BASE_TABLE_FINE_GRAINED_SECURITY_POLICY` (value: `"BASE_TABLE_FINE_GRAINED_SECURITY_POLICY"`)

* `BASE_TABLE_TOO_STALE` (value: `"BASE_TABLE_TOO_STALE"`)




