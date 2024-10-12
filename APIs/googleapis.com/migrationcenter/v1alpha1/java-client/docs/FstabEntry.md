

# FstabEntry

Single fstab entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_file** | **String** | The mount point for the filesystem. |  [optional] |
|**freq** | **Integer** | Used by dump to determine which filesystems need to be dumped. |  [optional] |
|**mntops** | **String** | Mount options associated with the filesystem. |  [optional] |
|**passno** | **Integer** | Used by the fsck(8) program to determine the order in which filesystem checks are done at reboot time. |  [optional] |
|**spec** | **String** | The block special device or remote filesystem to be mounted. |  [optional] |
|**vfstype** | **String** | The type of the filesystem. |  [optional] |



