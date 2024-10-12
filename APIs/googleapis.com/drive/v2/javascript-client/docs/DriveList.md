# GoogleDriveApi.DriveList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[Drive]**](Drive.md) | The list of shared drives. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. | [optional] 
**kind** | **String** | This is always &#x60;drive#driveList&#x60; | [optional] [default to &#39;drive#driveList&#39;]
**nextPageToken** | **String** | The page token for the next page of shared drives. This will be absent if the end of the list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. | [optional] 


