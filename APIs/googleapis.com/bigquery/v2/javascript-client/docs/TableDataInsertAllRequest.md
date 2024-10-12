# BigQueryApi.TableDataInsertAllRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignoreUnknownValues** | **Boolean** | Optional. Accept rows that contain values that do not match the schema. The unknown values are ignored. Default is false, which treats unknown values as errors. | [optional] 
**kind** | **String** | Optional. The resource type of the response. The value is not checked at the backend. Historically, it has been set to \&quot;bigquery#tableDataInsertAllRequest\&quot; but you are not required to set it. | [optional] [default to &#39;bigquery#tableDataInsertAllRequest&#39;]
**rows** | [**[TableDataInsertAllRequestRowsInner]**](TableDataInsertAllRequestRowsInner.md) |  | [optional] 
**skipInvalidRows** | **Boolean** | Optional. Insert all valid rows of a request, even if invalid rows exist. The default value is false, which causes the entire request to fail if any invalid rows exist. | [optional] 
**templateSuffix** | **String** | Optional. If specified, treats the destination table as a base template, and inserts the rows into an instance table named \&quot;{destination}{templateSuffix}\&quot;. BigQuery will manage creation of the instance table, using the schema of the base template table. See https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables for considerations when working with templates tables. | [optional] 
**traceId** | **String** | Optional. Unique request trace id. Used for debugging purposes only. It is case-sensitive, limited to up to 36 ASCII characters. A UUID is recommended. | [optional] 


