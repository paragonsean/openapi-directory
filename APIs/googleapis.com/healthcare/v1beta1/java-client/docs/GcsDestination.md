

# GcsDestination

The Cloud Storage output destination. The Cloud Healthcare Service Agent requires the `roles/storage.objectAdmin` Cloud IAM roles on the Cloud Storage location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentStructure** | [**ContentStructureEnum**](#ContentStructureEnum) | The format of the exported HL7v2 message files. |  [optional] |
|**messageView** | [**MessageViewEnum**](#MessageViewEnum) | Specifies the parts of the Message resource to include in the export. If not specified, FULL is used. |  [optional] |
|**uriPrefix** | **String** | URI of an existing Cloud Storage directory where the server writes result files, in the format &#x60;gs://{bucket-id}/{path/to/destination/dir}&#x60;. If there is no trailing slash, the service appends one when composing the object path. |  [optional] |



## Enum: ContentStructureEnum

| Name | Value |
|---- | -----|
| CONTENT_STRUCTURE_UNSPECIFIED | &quot;CONTENT_STRUCTURE_UNSPECIFIED&quot; |
| MESSAGE_JSON | &quot;MESSAGE_JSON&quot; |



## Enum: MessageViewEnum

| Name | Value |
|---- | -----|
| MESSAGE_VIEW_UNSPECIFIED | &quot;MESSAGE_VIEW_UNSPECIFIED&quot; |
| RAW_ONLY | &quot;RAW_ONLY&quot; |
| PARSED_ONLY | &quot;PARSED_ONLY&quot; |
| FULL | &quot;FULL&quot; |
| SCHEMATIZED_ONLY | &quot;SCHEMATIZED_ONLY&quot; |
| BASIC | &quot;BASIC&quot; |



