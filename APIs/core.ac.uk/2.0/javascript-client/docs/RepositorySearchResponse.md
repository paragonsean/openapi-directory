# CoreApiV2.RepositorySearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**[Repository]**](Repository.md) | Search results | [optional] 
**status** | **String** | Operation status | 
**totalHits** | **Number** | Total number of repositories matching the search criteria | 



## Enum: StatusEnum


* `OK` (value: `"OK"`)

* `Not found` (value: `"Not found"`)

* `Too many queries` (value: `"Too many queries"`)

* `Missing parameter` (value: `"Missing parameter"`)

* `Invalid parameter` (value: `"Invalid parameter"`)

* `Parameter out of bounds` (value: `"Parameter out of bounds"`)




