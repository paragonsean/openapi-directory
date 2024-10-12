# CloudStorageJsonApi.Objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[ModelObject]**](ModelObject.md) | The list of items. | [optional] 
**kind** | **String** | The kind of item this is. For lists of objects, this is always storage#objects. | [optional] [default to &#39;storage#objects&#39;]
**nextPageToken** | **String** | The continuation token, used to page through large result sets. Provide this value in a subsequent request to return the next page of results. | [optional] 
**prefixes** | **[String]** | The list of prefixes of objects matching-but-not-listed up to and including the requested delimiter. | [optional] 


