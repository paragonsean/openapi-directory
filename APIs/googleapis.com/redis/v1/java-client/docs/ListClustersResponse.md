

# ListClustersResponse

Response for ListClusters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusters** | [**List&lt;Cluster&gt;**](Cluster.md) | A list of Redis clusters in the project in the specified location, or across all locations. If the &#x60;location_id&#x60; in the parent field of the request is \&quot;-\&quot;, all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder Redis entry is included in the response with the &#x60;name&#x60; field set to a value of the form &#x60;projects/{project_id}/locations/{location_id}/clusters/&#x60;- and the &#x60;status&#x60; field set to ERROR and &#x60;status_message&#x60; field set to \&quot;location not available for ListClusters\&quot;. |  [optional] |
|**nextPageToken** | **String** | Token to retrieve the next page of results, or empty if there are no more results in the list. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



