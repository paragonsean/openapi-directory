# CloudDocumentAiApi.GoogleCloudDocumentaiV1ProcessorType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowCreation** | **Boolean** | Whether the processor type allows creation. If true, users can create a processor of this processor type. Otherwise, users need to request access. | [optional] 
**availableLocations** | [**[GoogleCloudDocumentaiV1ProcessorTypeLocationInfo]**](GoogleCloudDocumentaiV1ProcessorTypeLocationInfo.md) | The locations in which this processor is available. | [optional] 
**category** | **String** | The processor category, used by UI to group processor types. | [optional] 
**launchStage** | **String** | Launch stage of the processor type | [optional] 
**name** | **String** | The resource name of the processor type. Format: &#x60;projects/{project}/processorTypes/{processor_type}&#x60; | [optional] 
**sampleDocumentUris** | **[String]** | A set of Cloud Storage URIs of sample documents for this processor. | [optional] 
**type** | **String** | The processor type, such as: &#x60;OCR_PROCESSOR&#x60;, &#x60;INVOICE_PROCESSOR&#x60;. | [optional] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `PRELAUNCH` (value: `"PRELAUNCH"`)

* `EARLY_ACCESS` (value: `"EARLY_ACCESS"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)




