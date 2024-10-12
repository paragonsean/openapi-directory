# SensitiveDataProtectionDlp.GooglePrivacyDlpV2Deidentify

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudStorageOutput** | **String** | Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for cloud storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path. Form of: gs://bucket/folder/ or gs://bucket | [optional] 
**fileTypesToTransform** | **[String]** | List of user-specified file type groups to transform. If specified, only the files with these filetypes will be transformed. If empty, all supported files will be transformed. Supported types may be automatically added over time. If a file type is set in this field that isn&#39;t supported by the Deidentify action then the job will fail and will not be successfully created/started. Currently the only filetypes supported are: IMAGES, TEXT_FILES, CSV, TSV. | [optional] 
**transformationConfig** | [**GooglePrivacyDlpV2TransformationConfig**](GooglePrivacyDlpV2TransformationConfig.md) |  | [optional] 
**transformationDetailsStorageConfig** | [**GooglePrivacyDlpV2TransformationDetailsStorageConfig**](GooglePrivacyDlpV2TransformationDetailsStorageConfig.md) |  | [optional] 



## Enum: [FileTypesToTransformEnum]


* `FILE_TYPE_UNSPECIFIED` (value: `"FILE_TYPE_UNSPECIFIED"`)

* `BINARY_FILE` (value: `"BINARY_FILE"`)

* `TEXT_FILE` (value: `"TEXT_FILE"`)

* `IMAGE` (value: `"IMAGE"`)

* `WORD` (value: `"WORD"`)

* `PDF` (value: `"PDF"`)

* `AVRO` (value: `"AVRO"`)

* `CSV` (value: `"CSV"`)

* `TSV` (value: `"TSV"`)

* `POWERPOINT` (value: `"POWERPOINT"`)

* `EXCEL` (value: `"EXCEL"`)




