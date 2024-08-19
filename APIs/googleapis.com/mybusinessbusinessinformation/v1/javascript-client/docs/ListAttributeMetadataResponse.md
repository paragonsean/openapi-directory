# MyBusinessBusinessInformationApi.ListAttributeMetadataResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributeMetadata** | [**[AttributeMetadata]**](AttributeMetadata.md) | A collection of attribute metadata for the available attributes. | [optional] 
**nextPageToken** | **String** | If the number of attributes exceeded the requested page size, this field will be populated with a token to fetch the next page of attributes on a subsequent call to &#x60;attributes.list&#x60;. If there are no more attributes, this field will not be present in the response. | [optional] 


