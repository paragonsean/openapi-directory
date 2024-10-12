

# ModelFile

An individual file within a script project. A file is a third-party source code created by one or more developers. It can be a server-side JS code, HTML, or a configuration file. Each script project can contain multiple files.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Creation date timestamp. This read-only field is only visible to users who have WRITER permission for the script project. |  [optional] |
|**functionSet** | [**GoogleAppsScriptTypeFunctionSet**](GoogleAppsScriptTypeFunctionSet.md) |  |  [optional] |
|**lastModifyUser** | [**GoogleAppsScriptTypeUser**](GoogleAppsScriptTypeUser.md) |  |  [optional] |
|**name** | **String** | The name of the file. The file extension is not part of the file name, which can be identified from the type field. |  [optional] |
|**source** | **String** | The file content. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the file. |  [optional] |
|**updateTime** | **String** | Last modified date timestamp. This read-only field is only visible to users who have WRITER permission for the script project. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ENUM_TYPE_UNSPECIFIED | &quot;ENUM_TYPE_UNSPECIFIED&quot; |
| SERVER_JS | &quot;SERVER_JS&quot; |
| HTML | &quot;HTML&quot; |
| JSON | &quot;JSON&quot; |



