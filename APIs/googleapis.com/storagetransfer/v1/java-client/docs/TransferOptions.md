

# TransferOptions

TransferOptions define the actions to be performed on objects in a transfer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deleteObjectsFromSourceAfterTransfer** | **Boolean** | Whether objects should be deleted from the source after they are transferred to the sink. **Note:** This option and delete_objects_unique_in_sink are mutually exclusive. |  [optional] |
|**deleteObjectsUniqueInSink** | **Boolean** | Whether objects that exist only in the sink should be deleted. **Note:** This option and delete_objects_from_source_after_transfer are mutually exclusive. |  [optional] |
|**metadataOptions** | [**MetadataOptions**](MetadataOptions.md) |  |  [optional] |
|**overwriteObjectsAlreadyExistingInSink** | **Boolean** | When to overwrite objects that already exist in the sink. The default is that only objects that are different from the source are ovewritten. If true, all objects in the sink whose name matches an object in the source are overwritten with the source object. |  [optional] |
|**overwriteWhen** | [**OverwriteWhenEnum**](#OverwriteWhenEnum) | When to overwrite objects that already exist in the sink. If not set, overwrite behavior is determined by overwrite_objects_already_existing_in_sink. |  [optional] |



## Enum: OverwriteWhenEnum

| Name | Value |
|---- | -----|
| OVERWRITE_WHEN_UNSPECIFIED | &quot;OVERWRITE_WHEN_UNSPECIFIED&quot; |
| DIFFERENT | &quot;DIFFERENT&quot; |
| NEVER | &quot;NEVER&quot; |
| ALWAYS | &quot;ALWAYS&quot; |



