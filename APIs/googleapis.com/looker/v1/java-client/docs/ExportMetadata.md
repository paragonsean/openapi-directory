

# ExportMetadata

ExportMetadata represents the metadata of the exported artifacts. The metadata.json file in export artifact can be parsed as this message

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exportEncryptionKey** | [**ExportMetadataEncryptionKey**](ExportMetadataEncryptionKey.md) |  |  [optional] |
|**filePaths** | **List&lt;String&gt;** | List of files created as part of export artifact (excluding the metadata). The paths are relative to the folder containing the metadata. |  [optional] |
|**lookerEncryptionKey** | **String** | Looker encryption key, encrypted with the provided export encryption key. This value will only be populated if the looker instance uses Looker managed encryption instead of CMEK. |  [optional] |
|**lookerInstance** | **String** | Name of the exported instance. Format: projects/{project}/locations/{location}/instances/{instance} |  [optional] |
|**lookerPlatformEdition** | **String** | Platform edition of the exported instance. |  [optional] |
|**lookerVersion** | **String** | Version of instance when the export was created. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | The source type of the migration. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| SOURCE_UNSPECIFIED | &quot;SOURCE_UNSPECIFIED&quot; |
| LOOKER_CORE | &quot;LOOKER_CORE&quot; |
| LOOKER_ORIGINAL | &quot;LOOKER_ORIGINAL&quot; |



