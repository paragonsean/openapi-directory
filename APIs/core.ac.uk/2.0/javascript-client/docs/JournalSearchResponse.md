# CoreApiV2.JournalSearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**[Journal]**](Journal.md) | Search results | [optional] 
**status** | **String** | Operation status | 
**totalHits** | **Number** | Total number of journals matching the search criteria | 



## Enum: StatusEnum


* `OK` (value: `"OK"`)

* `NOT_FOUND` (value: `"NOT_FOUND"`)

* `TOO_MANY_QUERIES` (value: `"TOO_MANY_QUERIES"`)

* `MISSING_PARAMETER` (value: `"MISSING_PARAMETER"`)

* `INVALID_PARAMETER` (value: `"INVALID_PARAMETER"`)




