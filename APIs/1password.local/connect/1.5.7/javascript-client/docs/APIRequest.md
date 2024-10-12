# 1PasswordConnect.APIRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** |  | [optional] 
**actor** | [**APIRequestActor**](APIRequestActor.md) |  | [optional] 
**requestId** | **String** | The unique id used to identify a single request. | [optional] 
**resource** | [**APIRequestResource**](APIRequestResource.md) |  | [optional] 
**result** | **String** |  | [optional] 
**timestamp** | **Date** | The time at which the request was processed by the server. | [optional] [readonly] 



## Enum: ActionEnum


* `READ` (value: `"READ"`)

* `CREATE` (value: `"CREATE"`)

* `UPDATE` (value: `"UPDATE"`)

* `DELETE` (value: `"DELETE"`)





## Enum: ResultEnum


* `SUCCESS` (value: `"SUCCESS"`)

* `DENY` (value: `"DENY"`)




