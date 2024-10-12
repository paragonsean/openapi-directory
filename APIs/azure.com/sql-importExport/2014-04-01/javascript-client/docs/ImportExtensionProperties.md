# AzureSqlDatabaseImportExportSpec.ImportExtensionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operationMode** | **String** | The type of import operation being performed. This is always Import. | 
**administratorLogin** | **String** | The name of the SQL administrator. | 
**administratorLoginPassword** | **String** | The password of the SQL administrator. | 
**authenticationType** | **String** | The authentication type. | [optional] [default to &#39;SQL&#39;]
**storageKey** | **String** | The storage key to use.  If storage key type is SharedAccessKey, it must be preceded with a \&quot;?.\&quot; | 
**storageKeyType** | **String** | The type of the storage key to use. | 
**storageUri** | **String** | The storage uri to use. | 



## Enum: OperationModeEnum


* `Import` (value: `"Import"`)





## Enum: AuthenticationTypeEnum


* `SQL` (value: `"SQL"`)

* `ADPassword` (value: `"ADPassword"`)





## Enum: StorageKeyTypeEnum


* `StorageAccessKey` (value: `"StorageAccessKey"`)

* `SharedAccessKey` (value: `"SharedAccessKey"`)




