# GoogleCloudMemorystoreForRedisApi.ListInstancesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**[Instance]**](Instance.md) | A list of Redis instances in the project in the specified location, or across all locations. If the &#x60;location_id&#x60; in the parent field of the request is \&quot;-\&quot;, all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder Redis entry is included in the response with the &#x60;name&#x60; field set to a value of the form &#x60;projects/{project_id}/locations/{location_id}/instances/&#x60;- and the &#x60;status&#x60; field set to ERROR and &#x60;status_message&#x60; field set to \&quot;location not available for ListInstances\&quot;. | [optional] 
**nextPageToken** | **String** | Token to retrieve the next page of results, or empty if there are no more results in the list. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


