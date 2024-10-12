

# RestoreBackupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**linodeId** | **Integer** | The ID of the Linode to restore a Backup to.  |  |
|**overwrite** | **Boolean** | If True, deletes all Disks and Configs on the target Linode before restoring.  If False, and the Disk image size is larger than the available space on the Linode, an error message indicating insufficient space is returned.  |  [optional] |



