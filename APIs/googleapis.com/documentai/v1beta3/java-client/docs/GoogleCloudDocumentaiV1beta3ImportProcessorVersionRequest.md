

# GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequest

The request message for the ImportProcessorVersion method. The Document AI [Service Agent](https://cloud.google.com/iam/docs/service-agents) of the destination project must have [Document AI Editor role](https://cloud.google.com/document-ai/docs/access-control/iam-roles) on the source project. The destination project is specified as part of the parent field. The source project is specified as part of the source or external_processor_version_source field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalProcessorVersionSource** | [**GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequestExternalProcessorVersionSource**](GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequestExternalProcessorVersionSource.md) |  |  [optional] |
|**processorVersionSource** | **String** | The source processor version to import from. The source processor version and destination processor need to be in the same environment and region. |  [optional] |



