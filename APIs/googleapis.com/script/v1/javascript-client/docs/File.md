# AppsScriptApi.File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Creation date timestamp. This read-only field is only visible to users who have WRITER permission for the script project. | [optional] 
**functionSet** | [**GoogleAppsScriptTypeFunctionSet**](GoogleAppsScriptTypeFunctionSet.md) |  | [optional] 
**lastModifyUser** | [**GoogleAppsScriptTypeUser**](GoogleAppsScriptTypeUser.md) |  | [optional] 
**name** | **String** | The name of the file. The file extension is not part of the file name, which can be identified from the type field. | [optional] 
**source** | **String** | The file content. | [optional] 
**type** | **String** | The type of the file. | [optional] 
**updateTime** | **String** | Last modified date timestamp. This read-only field is only visible to users who have WRITER permission for the script project. | [optional] 



## Enum: TypeEnum


* `ENUM_TYPE_UNSPECIFIED` (value: `"ENUM_TYPE_UNSPECIFIED"`)

* `SERVER_JS` (value: `"SERVER_JS"`)

* `HTML` (value: `"HTML"`)

* `JSON` (value: `"JSON"`)




