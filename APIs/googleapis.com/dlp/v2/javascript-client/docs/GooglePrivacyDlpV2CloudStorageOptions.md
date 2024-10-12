# SensitiveDataProtectionDlp.GooglePrivacyDlpV2CloudStorageOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytesLimitPerFile** | **String** | Max number of bytes to scan from a file. If a scanned file&#39;s size is bigger than this value then the rest of the bytes are omitted. Only one of &#x60;bytes_limit_per_file&#x60; and &#x60;bytes_limit_per_file_percent&#x60; can be specified. This field can&#39;t be set if de-identification is requested. For certain file types, setting this field has no effect. For more information, see [Limits on bytes scanned per file](https://cloud.google.com/sensitive-data-protection/docs/supported-file-types#max-byte-size-per-file). | [optional] 
**bytesLimitPerFilePercent** | **Number** | Max percentage of bytes to scan from a file. The rest are omitted. The number of bytes scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. Only one of bytes_limit_per_file and bytes_limit_per_file_percent can be specified. This field can&#39;t be set if de-identification is requested. For certain file types, setting this field has no effect. For more information, see [Limits on bytes scanned per file](https://cloud.google.com/sensitive-data-protection/docs/supported-file-types#max-byte-size-per-file). | [optional] 
**fileSet** | [**GooglePrivacyDlpV2FileSet**](GooglePrivacyDlpV2FileSet.md) |  | [optional] 
**fileTypes** | **[String]** | List of file type groups to include in the scan. If empty, all files are scanned and available data format processors are applied. In addition, the binary content of the selected files is always scanned as well. Images are scanned only as binary if the specified region does not support image inspection and no file_types were specified. Image inspection is restricted to &#39;global&#39;, &#39;us&#39;, &#39;asia&#39;, and &#39;europe&#39;. | [optional] 
**filesLimitPercent** | **Number** | Limits the number of files to scan to this percentage of the input FileSet. Number of files scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. | [optional] 
**sampleMethod** | **String** | How to sample the data. | [optional] 



## Enum: [FileTypesEnum]


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





## Enum: SampleMethodEnum


* `SAMPLE_METHOD_UNSPECIFIED` (value: `"SAMPLE_METHOD_UNSPECIFIED"`)

* `TOP` (value: `"TOP"`)

* `RANDOM_START` (value: `"RANDOM_START"`)




