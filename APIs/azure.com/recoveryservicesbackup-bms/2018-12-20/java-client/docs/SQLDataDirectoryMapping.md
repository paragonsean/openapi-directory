

# SQLDataDirectoryMapping

Encapsulates information regarding data directory

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mappingType** | [**MappingTypeEnum**](#MappingTypeEnum) | Type of data directory mapping |  [optional] |
|**sourceLogicalName** | **String** | Restore source logical name path |  [optional] |
|**sourcePath** | **String** | Restore source path |  [optional] |
|**targetPath** | **String** | Target path |  [optional] |



## Enum: MappingTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DATA | &quot;Data&quot; |
| LOG | &quot;Log&quot; |



