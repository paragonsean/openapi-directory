# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3Processor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time the processor was created. | [optional] 
**defaultProcessorVersion** | **String** | The default processor version. | [optional] 
**displayName** | **String** | The display name of the processor. | [optional] 
**kmsKeyName** | **String** | The [KMS key](https://cloud.google.com/security-key-management) used for encryption and decryption in CMEK scenarios. | [optional] 
**name** | **String** | Output only. Immutable. The resource name of the processor. Format: &#x60;projects/{project}/locations/{location}/processors/{processor}&#x60; | [optional] [readonly] 
**processEndpoint** | **String** | Output only. Immutable. The http endpoint that can be called to invoke processing. | [optional] [readonly] 
**processorVersionAliases** | [**[GoogleCloudDocumentaiV1beta3ProcessorVersionAlias]**](GoogleCloudDocumentaiV1beta3ProcessorVersionAlias.md) | Output only. The processor version aliases. | [optional] [readonly] 
**state** | **String** | Output only. The state of the processor. | [optional] [readonly] 
**type** | **String** | The processor type, such as: &#x60;OCR_PROCESSOR&#x60;, &#x60;INVOICE_PROCESSOR&#x60;. To get a list of processor types, see FetchProcessorTypes. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)

* `ENABLING` (value: `"ENABLING"`)

* `DISABLING` (value: `"DISABLING"`)

* `CREATING` (value: `"CREATING"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)




