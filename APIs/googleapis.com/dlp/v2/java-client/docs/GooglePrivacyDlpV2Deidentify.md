

# GooglePrivacyDlpV2Deidentify

Create a de-identified copy of the requested table or files. A TransformationDetail will be created for each transformation. If any rows in BigQuery are skipped during de-identification (transformation errors or row size exceeds BigQuery insert API limits) they are placed in the failure output table. If the original row exceeds the BigQuery insert API limit it will be truncated when written to the failure output table. The failure output table can be set in the action.deidentify.output.big_query_output.deidentified_failure_output_table field, if no table is set, a table will be automatically created in the same project and dataset as the original table. Compatible with: Inspect

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudStorageOutput** | **String** | Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for cloud storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path. Form of: gs://bucket/folder/ or gs://bucket |  [optional] |
|**fileTypesToTransform** | [**List&lt;FileTypesToTransformEnum&gt;**](#List&lt;FileTypesToTransformEnum&gt;) | List of user-specified file type groups to transform. If specified, only the files with these filetypes will be transformed. If empty, all supported files will be transformed. Supported types may be automatically added over time. If a file type is set in this field that isn&#39;t supported by the Deidentify action then the job will fail and will not be successfully created/started. Currently the only filetypes supported are: IMAGES, TEXT_FILES, CSV, TSV. |  [optional] |
|**transformationConfig** | [**GooglePrivacyDlpV2TransformationConfig**](GooglePrivacyDlpV2TransformationConfig.md) |  |  [optional] |
|**transformationDetailsStorageConfig** | [**GooglePrivacyDlpV2TransformationDetailsStorageConfig**](GooglePrivacyDlpV2TransformationDetailsStorageConfig.md) |  |  [optional] |



## Enum: List&lt;FileTypesToTransformEnum&gt;

| Name | Value |
|---- | -----|
| FILE_TYPE_UNSPECIFIED | &quot;FILE_TYPE_UNSPECIFIED&quot; |
| BINARY_FILE | &quot;BINARY_FILE&quot; |
| TEXT_FILE | &quot;TEXT_FILE&quot; |
| IMAGE | &quot;IMAGE&quot; |
| WORD | &quot;WORD&quot; |
| PDF | &quot;PDF&quot; |
| AVRO | &quot;AVRO&quot; |
| CSV | &quot;CSV&quot; |
| TSV | &quot;TSV&quot; |
| POWERPOINT | &quot;POWERPOINT&quot; |
| EXCEL | &quot;EXCEL&quot; |



