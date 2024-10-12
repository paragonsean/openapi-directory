

# GuestConfigDetails

Guest OS config information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fstab** | [**FstabEntryList**](FstabEntryList.md) |  |  [optional] |
|**hosts** | [**HostsEntryList**](HostsEntryList.md) |  |  [optional] |
|**issue** | **String** | OS issue (typically /etc/issue in Linux). |  [optional] |
|**nfsExports** | [**NfsExportList**](NfsExportList.md) |  |  [optional] |
|**selinuxMode** | [**SelinuxModeEnum**](#SelinuxModeEnum) | Security-Enhanced Linux (SELinux) mode. |  [optional] |



## Enum: SelinuxModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SE_LINUX_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;SE_LINUX_MODE_DISABLED&quot; |
| PERMISSIVE | &quot;SE_LINUX_MODE_PERMISSIVE&quot; |
| ENFORCING | &quot;SE_LINUX_MODE_ENFORCING&quot; |



