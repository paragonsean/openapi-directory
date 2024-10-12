# CloudFilestoreApi.ListInstancesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**[Instance]**](Instance.md) | A list of instances in the project for the specified location. If the &#x60;{location}&#x60; value in the request is \&quot;-\&quot;, the response contains a list of instances from all locations. If any location is unreachable, the response will only return instances in reachable locations and the \&quot;unreachable\&quot; field will be populated with a list of unreachable locations. | [optional] 
**nextPageToken** | **String** | The token you can use to retrieve the next page of results. Not returned if there are no more results in the list. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


