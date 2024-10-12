

# GoogleCloudDocumentaiV1ProcessorType

A processor type is responsible for performing a certain document understanding task on a certain type of document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowCreation** | **Boolean** | Whether the processor type allows creation. If true, users can create a processor of this processor type. Otherwise, users need to request access. |  [optional] |
|**availableLocations** | [**List&lt;GoogleCloudDocumentaiV1ProcessorTypeLocationInfo&gt;**](GoogleCloudDocumentaiV1ProcessorTypeLocationInfo.md) | The locations in which this processor is available. |  [optional] |
|**category** | **String** | The processor category, used by UI to group processor types. |  [optional] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | Launch stage of the processor type |  [optional] |
|**name** | **String** | The resource name of the processor type. Format: &#x60;projects/{project}/processorTypes/{processor_type}&#x60; |  [optional] |
|**sampleDocumentUris** | **List&lt;String&gt;** | A set of Cloud Storage URIs of sample documents for this processor. |  [optional] |
|**type** | **String** | The processor type, such as: &#x60;OCR_PROCESSOR&#x60;, &#x60;INVOICE_PROCESSOR&#x60;. |  [optional] |



## Enum: LaunchStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| UNIMPLEMENTED | &quot;UNIMPLEMENTED&quot; |
| PRELAUNCH | &quot;PRELAUNCH&quot; |
| EARLY_ACCESS | &quot;EARLY_ACCESS&quot; |
| ALPHA | &quot;ALPHA&quot; |
| BETA | &quot;BETA&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



