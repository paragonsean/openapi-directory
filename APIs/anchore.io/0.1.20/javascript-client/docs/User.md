# AnchoreEngineApiServer.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The timestampt the user record was created | [optional] 
**lastUpdated** | **Date** | The timestamp of the last update to this record | [optional] 
**source** | **String** | If the user is external, this is the source that the user was initialized from. All other user types have this set to null | [optional] 
**type** | **String** | The user&#39;s type | [optional] 
**username** | **String** | The username to authenticate with | 



## Enum: TypeEnum


* `native` (value: `"native"`)

* `internal` (value: `"internal"`)

* `external` (value: `"external"`)




