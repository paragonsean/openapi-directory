# FrankieFinancialApi.DocumentSearchResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentSearchResults** | [**[DocumentSearchResultListItem]**](DocumentSearchResultListItem.md) | The list of (potentially) matching documents with confidence levels.  If you are the \&quot;owner\&quot; of the document - i.e. the same CustomerID and CustomerChildID (if relevant) - then the full details of the document will be returned, except for the contents of any attached scans. If you are not the owner of the document, then just the ID and confidence level is returned. You can still use this ID to retrieve any check results (see GET /document/{documentId}/checks)  | [optional] 
**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  | 


