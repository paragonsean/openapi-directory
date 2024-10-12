

# ListBareMetalClustersResponse

Response message for listing bare metal Clusters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bareMetalClusters** | [**List&lt;BareMetalCluster&gt;**](BareMetalCluster.md) | The list of bare metal Clusters. |  [optional] |
|**nextPageToken** | **String** | A token identifying a page of results the server should return. If the token is not empty this means that more results are available and should be retrieved by repeating the request with the provided page token. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



