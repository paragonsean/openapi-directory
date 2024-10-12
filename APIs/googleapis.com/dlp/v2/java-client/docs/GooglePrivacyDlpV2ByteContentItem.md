

# GooglePrivacyDlpV2ByteContentItem

Container for bytes to inspect or redact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **byte[]** | Content data to inspect or redact. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of data stored in the bytes string. Default will be TEXT_UTF8. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BYTES_TYPE_UNSPECIFIED | &quot;BYTES_TYPE_UNSPECIFIED&quot; |
| IMAGE | &quot;IMAGE&quot; |
| IMAGE_JPEG | &quot;IMAGE_JPEG&quot; |
| IMAGE_BMP | &quot;IMAGE_BMP&quot; |
| IMAGE_PNG | &quot;IMAGE_PNG&quot; |
| IMAGE_SVG | &quot;IMAGE_SVG&quot; |
| TEXT_UTF8 | &quot;TEXT_UTF8&quot; |
| WORD_DOCUMENT | &quot;WORD_DOCUMENT&quot; |
| PDF | &quot;PDF&quot; |
| POWERPOINT_DOCUMENT | &quot;POWERPOINT_DOCUMENT&quot; |
| EXCEL_DOCUMENT | &quot;EXCEL_DOCUMENT&quot; |
| AVRO | &quot;AVRO&quot; |
| CSV | &quot;CSV&quot; |
| TSV | &quot;TSV&quot; |



