# KubernetesEngineApi.ListUsableSubnetworksResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | This token allows you to get the next page of results for list requests. If the number of results is larger than &#x60;page_size&#x60;, use the &#x60;next_page_token&#x60; as a value for the query parameter &#x60;page_token&#x60; in the next request. The value will become empty when there are no more pages. | [optional] 
**subnetworks** | [**[UsableSubnetwork]**](UsableSubnetwork.md) | A list of usable subnetworks in the specified network project. | [optional] 


