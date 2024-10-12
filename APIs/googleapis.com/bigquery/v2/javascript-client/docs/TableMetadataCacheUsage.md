# BigQueryApi.TableMetadataCacheUsage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explanation** | **String** | Free form human-readable reason metadata caching was unused for the job. | [optional] 
**tableReference** | [**TableReference**](TableReference.md) |  | [optional] 
**tableType** | **String** | [Table type](/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.type). | [optional] 
**unusedReason** | **String** | Reason for not using metadata caching for the table. | [optional] 



## Enum: UnusedReasonEnum


* `UNUSED_REASON_UNSPECIFIED` (value: `"UNUSED_REASON_UNSPECIFIED"`)

* `EXCEEDED_MAX_STALENESS` (value: `"EXCEEDED_MAX_STALENESS"`)

* `METADATA_CACHING_NOT_ENABLED` (value: `"METADATA_CACHING_NOT_ENABLED"`)

* `OTHER_REASON` (value: `"OTHER_REASON"`)




