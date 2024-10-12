

# ImportResourcesRequest

Request to import resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentStructure** | [**ContentStructureEnum**](#ContentStructureEnum) | The content structure in the source location. If not specified, the server treats the input source files as BUNDLE. |  [optional] |
|**gcsSource** | [**GoogleCloudHealthcareV1FhirGcsSource**](GoogleCloudHealthcareV1FhirGcsSource.md) |  |  [optional] |



## Enum: ContentStructureEnum

| Name | Value |
|---- | -----|
| CONTENT_STRUCTURE_UNSPECIFIED | &quot;CONTENT_STRUCTURE_UNSPECIFIED&quot; |
| BUNDLE | &quot;BUNDLE&quot; |
| RESOURCE | &quot;RESOURCE&quot; |
| BUNDLE_PRETTY | &quot;BUNDLE_PRETTY&quot; |
| RESOURCE_PRETTY | &quot;RESOURCE_PRETTY&quot; |



