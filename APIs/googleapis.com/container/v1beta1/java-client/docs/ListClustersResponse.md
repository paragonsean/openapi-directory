

# ListClustersResponse

ListClustersResponse is the result of ListClustersRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusters** | [**List&lt;Cluster&gt;**](Cluster.md) | A list of clusters in the project in the specified zone, or across all ones. |  [optional] |
|**missingZones** | **List&lt;String&gt;** | If any zones are listed here, the list of clusters returned may be missing those zones. |  [optional] |



