# CloudHealthcareApi.ImportResourcesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentStructure** | **String** | The content structure in the source location. If not specified, the server treats the input source files as BUNDLE. | [optional] 
**gcsSource** | [**GoogleCloudHealthcareV1beta1FhirGcsSource**](GoogleCloudHealthcareV1beta1FhirGcsSource.md) |  | [optional] 



## Enum: ContentStructureEnum


* `CONTENT_STRUCTURE_UNSPECIFIED` (value: `"CONTENT_STRUCTURE_UNSPECIFIED"`)

* `BUNDLE` (value: `"BUNDLE"`)

* `RESOURCE` (value: `"RESOURCE"`)

* `BUNDLE_PRETTY` (value: `"BUNDLE_PRETTY"`)

* `RESOURCE_PRETTY` (value: `"RESOURCE_PRETTY"`)




