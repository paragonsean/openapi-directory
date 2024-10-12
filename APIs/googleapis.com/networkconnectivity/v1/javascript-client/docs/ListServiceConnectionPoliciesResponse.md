# NetworkConnectivityApi.ListServiceConnectionPoliciesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. | [optional] 
**serviceConnectionPolicies** | [**[ServiceConnectionPolicy]**](ServiceConnectionPolicy.md) | ServiceConnectionPolicies to be returned. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


