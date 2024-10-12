# BigQueryApi.AggregationThresholdPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privacyUnitColumns** | **[String]** | Optional. The privacy unit column(s) associated with this policy. For now, only one column per data source object (table, view) is allowed as a privacy unit column. Representing as a repeated field in metadata for extensibility to multiple columns in future. Duplicates and Repeated struct fields are not allowed. For nested fields, use dot notation (\&quot;outer.inner\&quot;) | [optional] 
**threshold** | **String** | Optional. The threshold for the \&quot;aggregation threshold\&quot; policy. | [optional] 


