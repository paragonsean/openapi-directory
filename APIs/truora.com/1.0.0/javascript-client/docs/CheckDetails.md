# ChecksApi.CheckDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkId** | **String** | Associated background check ID | 
**dataSet** | **String** | Details dataset | 
**databaseName** | **String** | Database name. Do not use this field to identify the database as its value may vary as the check is completed | 
**group** | **String** | table group type | 
**id** | **String** | Detail ID | 
**result** | **String** | Database result | 
**score** | **Number** | Partial detail score. Scores are aggregated later in the background check | 
**tables** | [**[Table]**](Table.md) | Query detailed information | 



## Enum: GroupEnum


* `profile` (value: `"profile"`)

* `legal` (value: `"legal"`)

* `affiliations` (value: `"affiliations"`)

* `vehicle` (value: `"vehicle"`)

* `global` (value: `"global"`)

* `media` (value: `"media"`)

* `unknown` (value: `"unknown"`)





## Enum: ResultEnum


* `pending` (value: `"pending"`)

* `found` (value: `"found"`)

* `not_found` (value: `"not_found"`)

* `error` (value: `"error"`)




