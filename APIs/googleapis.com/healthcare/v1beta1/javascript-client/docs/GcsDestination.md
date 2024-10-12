# CloudHealthcareApi.GcsDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentStructure** | **String** | The format of the exported HL7v2 message files. | [optional] 
**messageView** | **String** | Specifies the parts of the Message resource to include in the export. If not specified, FULL is used. | [optional] 
**uriPrefix** | **String** | URI of an existing Cloud Storage directory where the server writes result files, in the format &#x60;gs://{bucket-id}/{path/to/destination/dir}&#x60;. If there is no trailing slash, the service appends one when composing the object path. | [optional] 



## Enum: ContentStructureEnum


* `CONTENT_STRUCTURE_UNSPECIFIED` (value: `"CONTENT_STRUCTURE_UNSPECIFIED"`)

* `MESSAGE_JSON` (value: `"MESSAGE_JSON"`)





## Enum: MessageViewEnum


* `MESSAGE_VIEW_UNSPECIFIED` (value: `"MESSAGE_VIEW_UNSPECIFIED"`)

* `RAW_ONLY` (value: `"RAW_ONLY"`)

* `PARSED_ONLY` (value: `"PARSED_ONLY"`)

* `FULL` (value: `"FULL"`)

* `SCHEMATIZED_ONLY` (value: `"SCHEMATIZED_ONLY"`)

* `BASIC` (value: `"BASIC"`)




