

# GoogleCloudDiscoveryengineLoggingImportErrorContext

The error payload that is populated on LRO import APIs, including the following: * `google.cloud.discoveryengine.v1alpha.DocumentService.ImportDocuments` * `google.cloud.discoveryengine.v1alpha.UserEventService.ImportUserEvents`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | **String** | The detailed content which caused the error on importing a document. |  [optional] |
|**gcsPath** | **String** | Google Cloud Storage file path of the import source. Can be set for batch operation error. |  [optional] |
|**lineNumber** | **String** | Line number of the content in file. Should be empty for permission or batch operation error. |  [optional] |
|**operation** | **String** | The operation resource name of the LRO. |  [optional] |
|**userEvent** | **String** | The detailed content which caused the error on importing a user event. |  [optional] |



