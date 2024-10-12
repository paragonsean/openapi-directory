

# JobConfigurationExtract

JobConfigurationExtract configures a job that exports data from a BigQuery table into Google Cloud Storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compression** | **String** | Optional. The compression type to use for exported files. Possible values include DEFLATE, GZIP, NONE, SNAPPY, and ZSTD. The default value is NONE. Not all compression formats are support for all file formats. DEFLATE is only supported for Avro. ZSTD is only supported for Parquet. Not applicable when extracting models. |  [optional] |
|**destinationFormat** | **String** | Optional. The exported file format. Possible values include CSV, NEWLINE_DELIMITED_JSON, PARQUET, or AVRO for tables and ML_TF_SAVED_MODEL or ML_XGBOOST_BOOSTER for models. The default value for tables is CSV. Tables with nested or repeated fields cannot be exported as CSV. The default value for models is ML_TF_SAVED_MODEL. |  [optional] |
|**destinationUri** | **String** | [Pick one] DEPRECATED: Use destinationUris instead, passing only one URI as necessary. The fully-qualified Google Cloud Storage URI where the extracted table should be written. |  [optional] |
|**destinationUris** | **List&lt;String&gt;** | [Pick one] A list of fully-qualified Google Cloud Storage URIs where the extracted table should be written. |  [optional] |
|**fieldDelimiter** | **String** | Optional. When extracting data in CSV format, this defines the delimiter to use between fields in the exported data. Default is &#39;,&#39;. Not applicable when extracting models. |  [optional] |
|**modelExtractOptions** | [**ModelExtractOptions**](ModelExtractOptions.md) |  |  [optional] |
|**printHeader** | **Boolean** | Optional. Whether to print out a header row in the results. Default is true. Not applicable when extracting models. |  [optional] |
|**sourceModel** | [**ModelReference**](ModelReference.md) |  |  [optional] |
|**sourceTable** | [**TableReference**](TableReference.md) |  |  [optional] |
|**useAvroLogicalTypes** | **Boolean** | Whether to use logical types when extracting to AVRO format. Not applicable when extracting models. |  [optional] |



