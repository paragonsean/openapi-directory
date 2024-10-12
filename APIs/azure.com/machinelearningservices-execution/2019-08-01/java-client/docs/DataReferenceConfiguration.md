

# DataReferenceConfiguration

A class for managing DataReferenceConfiguration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataStoreName** | **String** | The name of the data store. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Operation on the datastore, mount, download, upload. |  [optional] |
|**overwrite** | **Boolean** | Whether to overwrite the data if existing. |  [optional] |
|**pathOnCompute** | **String** | The path on the compute target. |  [optional] |
|**pathOnDataStore** | **String** | Relative path on the datastore. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MOUNT | &quot;Mount&quot; |
| DOWNLOAD | &quot;Download&quot; |
| UPLOAD | &quot;Upload&quot; |



