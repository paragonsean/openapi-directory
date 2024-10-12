

# ListConnectionsResponse

Response message for BeyondCorp.ListConnections.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connections** | [**List&lt;Connection&gt;**](Connection.md) | A list of BeyondCorp Connections in the project. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results, or empty if there are no more results in the list. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of locations that could not be reached. |  [optional] |



