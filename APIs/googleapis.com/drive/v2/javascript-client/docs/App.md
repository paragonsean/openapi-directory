# GoogleDriveApi.App

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized** | **Boolean** | Whether the app is authorized to access data on the user&#39;s Drive. | [optional] 
**createInFolderTemplate** | **String** | The template url to create a new file with this app in a given folder. The template will contain {folderId} to be replaced by the folder to create the new file in. | [optional] 
**createUrl** | **String** | The url to create a new file with this app. | [optional] 
**hasDriveWideScope** | **Boolean** | Whether the app has drive-wide scope. An app with drive-wide scope can access all files in the user&#39;s drive. | [optional] 
**icons** | [**[AppIconsInner]**](AppIconsInner.md) | The various icons for the app. | [optional] 
**id** | **String** | The ID of the app. | [optional] 
**installed** | **Boolean** | Whether the app is installed. | [optional] 
**kind** | **String** | This is always &#x60;drive#app&#x60;. | [optional] [default to &#39;drive#app&#39;]
**longDescription** | **String** | A long description of the app. | [optional] 
**name** | **String** | The name of the app. | [optional] 
**objectType** | **String** | The type of object this app creates (e.g. Chart). If empty, the app name should be used instead. | [optional] 
**openUrlTemplate** | **String** | The template url for opening files with this app. The template will contain &#x60;{ids}&#x60; and/or &#x60;{exportIds}&#x60; to be replaced by the actual file ids. See Open Files for the full documentation. | [optional] 
**primaryFileExtensions** | **[String]** | The list of primary file extensions. | [optional] 
**primaryMimeTypes** | **[String]** | The list of primary mime types. | [optional] 
**productId** | **String** | The ID of the product listing for this app. | [optional] 
**productUrl** | **String** | A link to the product listing for this app. | [optional] 
**secondaryFileExtensions** | **[String]** | The list of secondary file extensions. | [optional] 
**secondaryMimeTypes** | **[String]** | The list of secondary mime types. | [optional] 
**shortDescription** | **String** | A short description of the app. | [optional] 
**supportsCreate** | **Boolean** | Whether this app supports creating new objects. | [optional] 
**supportsImport** | **Boolean** | Whether this app supports importing from Docs Editors. | [optional] 
**supportsMultiOpen** | **Boolean** | Whether this app supports opening more than one file. | [optional] 
**supportsOfflineCreate** | **Boolean** | Whether this app supports creating new files when offline. | [optional] 
**useByDefault** | **Boolean** | Whether the app is selected as the default handler for the types it supports. | [optional] 


