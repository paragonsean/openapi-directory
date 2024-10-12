# OsdbRestApiV1.EntryPointParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A short description of the parameter for use in the OSDB Action Console. Optional - may be null. | 
**displayName** | **String** | The parameter&#39;s display name in the OSDB Action Console. Optional - may be null. | 
**parameterName** | **String** | The parameter name as present in the HTTP request. e.g. the key name in a query string key-value pair. | 
**permittedValues** | **[String]** | If the parameter accepts only a limited set of values, the allowed set of values. Null if not applicable. | 
**required** | **Number** | A flag indicating if the parameter is optional. | 
**type** | **String** | The type of the parameter, indicating its location in the HTTP request. | 



## Enum: TypeEnum


* `query` (value: `"query"`)

* `header` (value: `"header"`)

* `uri` (value: `"uri"`)

* `path` (value: `"path"`)

* `body` (value: `"body"`)




