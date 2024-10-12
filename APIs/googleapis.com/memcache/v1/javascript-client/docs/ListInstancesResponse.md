# CloudMemorystoreForMemcachedApi.ListInstancesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**[Instance]**](Instance.md) | A list of Memcached instances in the project in the specified location, or across all locations. If the &#x60;location_id&#x60; in the parent field of the request is \&quot;-\&quot;, all regions available to the project are queried, and the results aggregated. | [optional] 
**nextPageToken** | **String** | Token to retrieve the next page of results, or empty if there are no more results in the list. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


