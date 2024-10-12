

# RetentionPolicy

RetentionPolicy defines a Backup retention policy for a BackupPlan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupDeleteLockDays** | **Integer** | Optional. Minimum age for Backups created via this BackupPlan (in days). This field MUST be an integer value between 0-90 (inclusive). A Backup created under this BackupPlan will NOT be deletable until it reaches Backup&#39;s (create_time + backup_delete_lock_days). Updating this field of a BackupPlan does NOT affect existing Backups under it. Backups created AFTER a successful update will inherit the new value. Default: 0 (no delete blocking) |  [optional] |
|**backupRetainDays** | **Integer** | Optional. The default maximum age of a Backup created via this BackupPlan. This field MUST be an integer value &gt;&#x3D; 0 and &lt;&#x3D; 365. If specified, a Backup created under this BackupPlan will be automatically deleted after its age reaches (create_time + backup_retain_days). If not specified, Backups created under this BackupPlan will NOT be subject to automatic deletion. Updating this field does NOT affect existing Backups under it. Backups created AFTER a successful update will automatically pick up the new value. NOTE: backup_retain_days must be &gt;&#x3D; backup_delete_lock_days. If cron_schedule is defined, then this must be &lt;&#x3D; 360 * the creation interval. If rpo_config is defined, then this must be &lt;&#x3D; 360 * target_rpo_minutes / (1440minutes/day). Default: 0 (no automatic deletion) |  [optional] |
|**locked** | **Boolean** | Optional. This flag denotes whether the retention policy of this BackupPlan is locked. If set to True, no further update is allowed on this policy, including the &#x60;locked&#x60; field itself. Default: False |  [optional] |



