# MigrationCenterApi.GuestConfigDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fstab** | [**FstabEntryList**](FstabEntryList.md) |  | [optional] 
**hosts** | [**HostsEntryList**](HostsEntryList.md) |  | [optional] 
**issue** | **String** | OS issue (typically /etc/issue in Linux). | [optional] 
**nfsExports** | [**NfsExportList**](NfsExportList.md) |  | [optional] 
**selinuxMode** | **String** | Security-Enhanced Linux (SELinux) mode. | [optional] 



## Enum: SelinuxModeEnum


* `UNSPECIFIED` (value: `"SE_LINUX_MODE_UNSPECIFIED"`)

* `DISABLED` (value: `"SE_LINUX_MODE_DISABLED"`)

* `PERMISSIVE` (value: `"SE_LINUX_MODE_PERMISSIVE"`)

* `ENFORCING` (value: `"SE_LINUX_MODE_ENFORCING"`)




