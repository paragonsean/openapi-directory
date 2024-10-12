# RubrikRestApi.FilesetTemplatePatch

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
**id** | **String** |  | 
**includes** | **[String]** |  | [optional] 
**name** | **String** |  | [optional] 
**operatingSystemType** | **String** | Operating system type of filesets created by template. | [optional] 
**postBackupScript** | **String** | Script to run after backup of this Fileset ends. | [optional] 
**preBackupScript** | **String** | Script to run before backup of this Fileset starts. | [optional] 
**shareType** | **String** |  | [optional] 



## Enum: OperatingSystemTypeEnum


* `UnixLike` (value: `"UnixLike"`)

* `Windows` (value: `"Windows"`)





## Enum: ShareTypeEnum


* `NFS` (value: `"NFS"`)

* `SMB` (value: `"SMB"`)




