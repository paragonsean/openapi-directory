

# FilesetTemplatePatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowBackupHiddenFoldersInNetworkMounts** | **Boolean** | Include or exclude hidden folders inside locally-mounted remote file systems from backups. |  [optional] |
|**allowBackupNetworkMounts** | **Boolean** | Include or exclude locally-mounted remote file systems from backups. |  [optional] |
|**useWindowsVss** | **Boolean** | Use VSS during Windows backups. |  [optional] |
|**backupScriptErrorHandling** | **String** | Action taken if script fails. Options are \&quot;abort\&quot;, \&quot;continue\&quot;. |  [optional] |
|**backupScriptTimeout** | **Long** | Number of seconds after which the script is killed if it has not completed execution. |  [optional] |
|**exceptions** | **List&lt;String&gt;** |  |  [optional] |
|**excludes** | **List&lt;String&gt;** |  |  [optional] |
|**id** | **String** |  |  |
|**includes** | **List&lt;String&gt;** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**operatingSystemType** | [**OperatingSystemTypeEnum**](#OperatingSystemTypeEnum) | Operating system type of filesets created by template. |  [optional] |
|**postBackupScript** | **String** | Script to run after backup of this Fileset ends. |  [optional] |
|**preBackupScript** | **String** | Script to run before backup of this Fileset starts. |  [optional] |
|**shareType** | [**ShareTypeEnum**](#ShareTypeEnum) |  |  [optional] |



## Enum: OperatingSystemTypeEnum

| Name | Value |
|---- | -----|
| UNIX_LIKE | &quot;UnixLike&quot; |
| WINDOWS | &quot;Windows&quot; |



## Enum: ShareTypeEnum

| Name | Value |
|---- | -----|
| NFS | &quot;NFS&quot; |
| SMB | &quot;SMB&quot; |



