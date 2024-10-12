

# App

The `apps` resource provides a list of apps that a user has installed, with information about each app's supported MIME types, file extensions, and other details. Some resource methods (such as `apps.get`) require an `appId`. Use the `apps.list` method to retrieve the ID for an installed application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorized** | **Boolean** | Whether the app is authorized to access data on the user&#39;s Drive. |  [optional] |
|**createInFolderTemplate** | **String** | The template URL to create a file with this app in a given folder. The template contains the {folderId} to be replaced by the folder ID house the new file. |  [optional] |
|**createUrl** | **String** | The URL to create a file with this app. |  [optional] |
|**hasDriveWideScope** | **Boolean** | Whether the app has Drive-wide scope. An app with Drive-wide scope can access all files in the user&#39;s Drive. |  [optional] |
|**icons** | [**List&lt;AppIcons&gt;**](AppIcons.md) | The various icons for the app. |  [optional] |
|**id** | **String** | The ID of the app. |  [optional] |
|**installed** | **Boolean** | Whether the app is installed. |  [optional] |
|**kind** | **String** | Output only. Identifies what kind of resource this is. Value: the fixed string \&quot;drive#app\&quot;. |  [optional] |
|**longDescription** | **String** | A long description of the app. |  [optional] |
|**name** | **String** | The name of the app. |  [optional] |
|**objectType** | **String** | The type of object this app creates such as a Chart. If empty, the app name should be used instead. |  [optional] |
|**openUrlTemplate** | **String** | The template URL for opening files with this app. The template contains {ids} or {exportIds} to be replaced by the actual file IDs. For more information, see Open Files for the full documentation. |  [optional] |
|**primaryFileExtensions** | **List&lt;String&gt;** | The list of primary file extensions. |  [optional] |
|**primaryMimeTypes** | **List&lt;String&gt;** | The list of primary MIME types. |  [optional] |
|**productId** | **String** | The ID of the product listing for this app. |  [optional] |
|**productUrl** | **String** | A link to the product listing for this app. |  [optional] |
|**secondaryFileExtensions** | **List&lt;String&gt;** | The list of secondary file extensions. |  [optional] |
|**secondaryMimeTypes** | **List&lt;String&gt;** | The list of secondary MIME types. |  [optional] |
|**shortDescription** | **String** | A short description of the app. |  [optional] |
|**supportsCreate** | **Boolean** | Whether this app supports creating objects. |  [optional] |
|**supportsImport** | **Boolean** | Whether this app supports importing from Google Docs. |  [optional] |
|**supportsMultiOpen** | **Boolean** | Whether this app supports opening more than one file. |  [optional] |
|**supportsOfflineCreate** | **Boolean** | Whether this app supports creating files when offline. |  [optional] |
|**useByDefault** | **Boolean** | Whether the app is selected as the default handler for the types it supports. |  [optional] |



