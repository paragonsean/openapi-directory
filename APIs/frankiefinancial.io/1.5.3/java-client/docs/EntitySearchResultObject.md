

# EntitySearchResultObject

Contains the results of a given entity search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entitySearchResults** | [**List&lt;EntitySearchResultListItem&gt;**](EntitySearchResultListItem.md) | The list of (potentially) matching entities with confidence levels.  If you are the \&quot;owner\&quot; of the entity - i.e. the same CustomerID and CustomerChildID (if relevant) - then the full details of the entity and any owned documents will be returned, except for the contents of any attached scans.  If you are not the owner of the entity (or linked documents), then just the ID and confidence level is returned. You can still use this ID to retrieve any check results (see GET  /entity/{entityId}/checks and GET /document/{documentId}/checks)  |  [optional] |
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  |



