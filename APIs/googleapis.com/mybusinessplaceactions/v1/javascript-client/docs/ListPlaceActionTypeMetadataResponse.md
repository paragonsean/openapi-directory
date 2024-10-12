# MyBusinessPlaceActionsApi.ListPlaceActionTypeMetadataResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | If the number of action types exceeded the requested page size, this field will be populated with a token to fetch the next page on a subsequent call to &#x60;placeActionTypeMetadata.list&#x60;. If there are no more results, this field will not be present in the response. | [optional] 
**placeActionTypeMetadata** | [**[PlaceActionTypeMetadata]**](PlaceActionTypeMetadata.md) | A collection of metadata for the available place action types. | [optional] 


