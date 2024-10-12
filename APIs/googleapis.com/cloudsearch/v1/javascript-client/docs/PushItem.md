# CloudSearchApi.PushItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentHash** | **String** | Content hash of the item according to the repository. If specified, this is used to determine how to modify this item&#39;s status. Setting this field and the type field results in argument error. The maximum length is 2048 characters. | [optional] 
**metadataHash** | **String** | The metadata hash of the item according to the repository. If specified, this is used to determine how to modify this item&#39;s status. Setting this field and the type field results in argument error. The maximum length is 2048 characters. | [optional] 
**payload** | **Blob** | Provides additional document state information for the connector, such as an alternate repository ID and other metadata. The maximum length is 8192 bytes. | [optional] 
**queue** | **String** | Queue to which this item belongs. The &#x60;default&#x60; queue is chosen if this field is not specified. The maximum length is 512 characters. | [optional] 
**repositoryError** | [**RepositoryError**](RepositoryError.md) |  | [optional] 
**structuredDataHash** | **String** | Structured data hash of the item according to the repository. If specified, this is used to determine how to modify this item&#39;s status. Setting this field and the type field results in argument error. The maximum length is 2048 characters. | [optional] 
**type** | **String** | The type of the push operation that defines the push behavior. | [optional] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `MODIFIED` (value: `"MODIFIED"`)

* `NOT_MODIFIED` (value: `"NOT_MODIFIED"`)

* `REPOSITORY_ERROR` (value: `"REPOSITORY_ERROR"`)

* `REQUEUE` (value: `"REQUEUE"`)




