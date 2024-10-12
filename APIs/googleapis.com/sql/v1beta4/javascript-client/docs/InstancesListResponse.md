# CloudSqlAdminApi.InstancesListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[DatabaseInstance]**](DatabaseInstance.md) | List of database instance resources. | [optional] 
**kind** | **String** | This is always &#x60;sql#instancesList&#x60;. | [optional] 
**nextPageToken** | **String** | The continuation token, used to page through large result sets. Provide this value in a subsequent request to return the next page of results. | [optional] 
**warnings** | [**[ApiWarning]**](ApiWarning.md) | List of warnings that occurred while handling the request. | [optional] 


