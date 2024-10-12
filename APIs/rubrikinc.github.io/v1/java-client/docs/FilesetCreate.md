

# FilesetCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arraySpec** | [**FilesetArraySpec**](FilesetArraySpec.md) |  |  [optional] |
|**enableHardlinkSupport** | **Boolean** | A Boolean value that determines whether to recognize and dedupe hardlinks in a fileset. When &#39;true,&#39; performs a hardlink deduplication. When &#39;false,&#39; performs a normal backup that treats hardlinks as normal files. If not specified, this defaults to false. |  [optional] |
|**enableSymlinkResolution** | **Boolean** | A Boolean value that determines whether to resolve symlink in a fileset. When &#39;true,&#39; performs a symlink resolution. When &#39;false,&#39; performs no symlink resolution. If not specified, this defaults to false. |  [optional] |
|**failoverClusterAppId** | **String** | ID of the failover cluster app. |  [optional] |
|**hostId** | **String** |  |  [optional] |
|**isPassthrough** | **Boolean** | A Boolean value that determines whether to take a direct archive backup. When &#39;true,&#39; performs a direct archive backup. When &#39;false,&#39; performs a normal backup. If not specified, this defaults to false. |  [optional] |
|**shareId** | **String** |  |  [optional] |
|**snapMirrorLabelForFullBackup** | **String** | Rubrik CDM uses a prefix match to select the latest SnapMirror snapshot that matches this value during a full backup of a SnapMirror destination share. |  [optional] |
|**snapMirrorLabelForIncrementalBackup** | **String** | Rubrik CDM selects the latest SnapMirror snapshot that matches this value using a prefix match during an incremental backup of a SnapMirror destination share. |  [optional] |
|**templateId** | **String** |  |  |



