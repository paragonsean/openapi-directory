

# GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataImportConfigValidationResult

The validation status of each import config. Status is set to an error if there are no documents to import in the `import_config`, or `OK` if the operation will try to proceed with at least one document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputGcsSource** | **String** | The source Cloud Storage URI specified in the import config. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |



