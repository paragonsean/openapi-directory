# RubrikRestApi.FilesetTemplateCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowBackupHiddenFoldersInNetworkMounts** | **Boolean** | Include or exclude hidden folders inside locally-mounted remote file systems from backups. | [optional] 
**allowBackupNetworkMounts** | **Boolean** | Include or exclude locally-mounted remote file systems from backups. | [optional] 
**useWindowsVss** | **Boolean** | Use VSS during Windows backups. | [optional] 
**backupScriptErrorHandling** | **String** | Action taken if script fails. Options are \&quot;abort\&quot;, \&quot;continue\&quot;. | [optional] 
**backupScriptTimeout** | **Number** | Number of seconds after which the script is killed if it has not completed execution. | [optional] 
**exceptions** | **[String]** |  | [optional] 
**excludes** | **[String]** |  | [optional] 
**includes** | **[String]** |  | 
**isArrayEnabled** | **Boolean** | Boolean value that determines whether the fileset is array-enabled. Set to true to indicate that the fileset is array-enabled. Set to false to indicate that the fileset is not array-enabled. When a fileset is array-enabled, the includes must be top-level LVM logical volume mount points. | [optional] 
**name** | **String** |  | 
**operatingSystemType** | **String** | Operating system type of filesets created by template. | [optional] 
**postBackupScript** | **String** | Script to run after backup of this fileset ends. | [optional] 
**preBackupScript** | **String** | Script to run before backup of this fileset starts. | [optional] 
**shareType** | **String** |  | [optional] 



## Enum: OperatingSystemTypeEnum


* `UnixLike` (value: `"UnixLike"`)

* `Windows` (value: `"Windows"`)





## Enum: ShareTypeEnum


* `NFS` (value: `"NFS"`)

* `SMB` (value: `"SMB"`)




