# MessagingApiV3X.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Unique code of the error | 
**field** | **String** | The field that caused the error | [optional] 
**issue** | **String** | The reason for the error | 
**link** | **String** | URI for detailed information related to this error for the developer. | [optional] 
**location** | **String** | The location of the field that caused the error. | [optional] 
**suggestedAction** | **String** | Suggest practical actions for this particular issue. | 
**value** | **String** | The value of the field that caused the error | [optional] 



## Enum: LocationEnum


* `body` (value: `"body"`)

* `path` (value: `"path"`)

* `query` (value: `"query"`)




