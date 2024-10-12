

# TransportTrelloJsonldPost

The TransportTrello resource is a collection of transports that carry dispatched alerts to the external Trello service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |
|**trelloApiKey** | **String** | The API key for the Trello service. |  |
|**trelloApiToken** | **String** | The API token for the Trello service. Stored in encrypted format. |  |
|**trelloListId** | **String** | The list ID for the Trello service. |  |



