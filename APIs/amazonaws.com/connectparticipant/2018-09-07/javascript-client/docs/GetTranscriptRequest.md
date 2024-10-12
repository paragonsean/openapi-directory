# AmazonConnectParticipantService.GetTranscriptRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactId** | **String** | The contactId from the current contact chain for which transcript is needed. | [optional] 
**maxResults** | **Number** | The maximum number of results to return in the page. Default: 10.  | [optional] 
**nextToken** | **String** | The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results. | [optional] 
**scanDirection** | **String** | The direction from StartPosition from which to retrieve message. Default: BACKWARD when no StartPosition is provided, FORWARD with StartPosition.  | [optional] 
**sortOrder** | **String** | The sort order for the records. Default: DESCENDING. | [optional] 
**startPosition** | [**GetTranscriptRequestStartPosition**](GetTranscriptRequestStartPosition.md) |  | [optional] 



## Enum: ScanDirectionEnum


* `FORWARD` (value: `"FORWARD"`)

* `BACKWARD` (value: `"BACKWARD"`)





## Enum: SortOrderEnum


* `DESCENDING` (value: `"DESCENDING"`)

* `ASCENDING` (value: `"ASCENDING"`)




