# SensitiveDataProtectionDlp.GooglePrivacyDlpV2OutputStorageConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputSchema** | **String** | Schema used for writing the findings for Inspect jobs. This field is only used for Inspect and must be unspecified for Risk jobs. Columns are derived from the &#x60;Finding&#x60; object. If appending to an existing table, any columns from the predefined schema that are missing will be added. No columns in the existing table will be deleted. If unspecified, then all available columns will be used for a new table or an (existing) table with no schema, and no changes will be made to an existing table that has a schema. Only for use with external storage. | [optional] 
**table** | [**GooglePrivacyDlpV2BigQueryTable**](GooglePrivacyDlpV2BigQueryTable.md) |  | [optional] 



## Enum: OutputSchemaEnum


* `OUTPUT_SCHEMA_UNSPECIFIED` (value: `"OUTPUT_SCHEMA_UNSPECIFIED"`)

* `BASIC_COLUMNS` (value: `"BASIC_COLUMNS"`)

* `GCS_COLUMNS` (value: `"GCS_COLUMNS"`)

* `DATASTORE_COLUMNS` (value: `"DATASTORE_COLUMNS"`)

* `BIG_QUERY_COLUMNS` (value: `"BIG_QUERY_COLUMNS"`)

* `ALL_COLUMNS` (value: `"ALL_COLUMNS"`)




