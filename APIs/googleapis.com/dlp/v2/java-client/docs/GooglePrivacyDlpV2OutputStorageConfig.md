

# GooglePrivacyDlpV2OutputStorageConfig

Cloud repository for storing output.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outputSchema** | [**OutputSchemaEnum**](#OutputSchemaEnum) | Schema used for writing the findings for Inspect jobs. This field is only used for Inspect and must be unspecified for Risk jobs. Columns are derived from the &#x60;Finding&#x60; object. If appending to an existing table, any columns from the predefined schema that are missing will be added. No columns in the existing table will be deleted. If unspecified, then all available columns will be used for a new table or an (existing) table with no schema, and no changes will be made to an existing table that has a schema. Only for use with external storage. |  [optional] |
|**table** | [**GooglePrivacyDlpV2BigQueryTable**](GooglePrivacyDlpV2BigQueryTable.md) |  |  [optional] |



## Enum: OutputSchemaEnum

| Name | Value |
|---- | -----|
| OUTPUT_SCHEMA_UNSPECIFIED | &quot;OUTPUT_SCHEMA_UNSPECIFIED&quot; |
| BASIC_COLUMNS | &quot;BASIC_COLUMNS&quot; |
| GCS_COLUMNS | &quot;GCS_COLUMNS&quot; |
| DATASTORE_COLUMNS | &quot;DATASTORE_COLUMNS&quot; |
| BIG_QUERY_COLUMNS | &quot;BIG_QUERY_COLUMNS&quot; |
| ALL_COLUMNS | &quot;ALL_COLUMNS&quot; |



