

# ListConnectorsResponse

Response message for BeyondCorp.ListConnectors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectors** | [**List&lt;Connector&gt;**](Connector.md) | A list of BeyondCorp Connectors in the project. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results, or empty if there are no more results in the list. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of locations that could not be reached. |  [optional] |



