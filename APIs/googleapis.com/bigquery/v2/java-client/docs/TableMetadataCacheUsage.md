

# TableMetadataCacheUsage

Table level detail on the usage of metadata caching. Only set for Metadata caching eligible tables referenced in the query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**explanation** | **String** | Free form human-readable reason metadata caching was unused for the job. |  [optional] |
|**tableReference** | [**TableReference**](TableReference.md) |  |  [optional] |
|**tableType** | **String** | [Table type](/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.type). |  [optional] |
|**unusedReason** | [**UnusedReasonEnum**](#UnusedReasonEnum) | Reason for not using metadata caching for the table. |  [optional] |



## Enum: UnusedReasonEnum

| Name | Value |
|---- | -----|
| UNUSED_REASON_UNSPECIFIED | &quot;UNUSED_REASON_UNSPECIFIED&quot; |
| EXCEEDED_MAX_STALENESS | &quot;EXCEEDED_MAX_STALENESS&quot; |
| METADATA_CACHING_NOT_ENABLED | &quot;METADATA_CACHING_NOT_ENABLED&quot; |
| OTHER_REASON | &quot;OTHER_REASON&quot; |



