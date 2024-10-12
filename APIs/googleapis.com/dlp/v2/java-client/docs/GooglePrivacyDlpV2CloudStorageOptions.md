

# GooglePrivacyDlpV2CloudStorageOptions

Options defining a file or a set of files within a Cloud Storage bucket.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesLimitPerFile** | **String** | Max number of bytes to scan from a file. If a scanned file&#39;s size is bigger than this value then the rest of the bytes are omitted. Only one of &#x60;bytes_limit_per_file&#x60; and &#x60;bytes_limit_per_file_percent&#x60; can be specified. This field can&#39;t be set if de-identification is requested. For certain file types, setting this field has no effect. For more information, see [Limits on bytes scanned per file](https://cloud.google.com/sensitive-data-protection/docs/supported-file-types#max-byte-size-per-file). |  [optional] |
|**bytesLimitPerFilePercent** | **Integer** | Max percentage of bytes to scan from a file. The rest are omitted. The number of bytes scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. Only one of bytes_limit_per_file and bytes_limit_per_file_percent can be specified. This field can&#39;t be set if de-identification is requested. For certain file types, setting this field has no effect. For more information, see [Limits on bytes scanned per file](https://cloud.google.com/sensitive-data-protection/docs/supported-file-types#max-byte-size-per-file). |  [optional] |
|**fileSet** | [**GooglePrivacyDlpV2FileSet**](GooglePrivacyDlpV2FileSet.md) |  |  [optional] |
|**fileTypes** | [**List&lt;FileTypesEnum&gt;**](#List&lt;FileTypesEnum&gt;) | List of file type groups to include in the scan. If empty, all files are scanned and available data format processors are applied. In addition, the binary content of the selected files is always scanned as well. Images are scanned only as binary if the specified region does not support image inspection and no file_types were specified. Image inspection is restricted to &#39;global&#39;, &#39;us&#39;, &#39;asia&#39;, and &#39;europe&#39;. |  [optional] |
|**filesLimitPercent** | **Integer** | Limits the number of files to scan to this percentage of the input FileSet. Number of files scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. |  [optional] |
|**sampleMethod** | [**SampleMethodEnum**](#SampleMethodEnum) | How to sample the data. |  [optional] |



## Enum: List&lt;FileTypesEnum&gt;

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



## Enum: SampleMethodEnum

| Name | Value |
|---- | -----|
| SAMPLE_METHOD_UNSPECIFIED | &quot;SAMPLE_METHOD_UNSPECIFIED&quot; |
| TOP | &quot;TOP&quot; |
| RANDOM_START | &quot;RANDOM_START&quot; |



