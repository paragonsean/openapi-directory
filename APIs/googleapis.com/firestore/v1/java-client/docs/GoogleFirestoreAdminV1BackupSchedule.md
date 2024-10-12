

# GoogleFirestoreAdminV1BackupSchedule

A backup schedule for a Cloud Firestore Database. This resource is owned by the database it is backing up, and is deleted along with the database. The actual backups are not though.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp at which this backup schedule was created and effective since. No backups will be created for this schedule before this time. |  [optional] [readonly] |
|**dailyRecurrence** | **Object** | Represent a recurring schedule that runs at a specific time every day. The time zone is UTC. |  [optional] |
|**name** | **String** | Output only. The unique backup schedule identifier across all locations and databases for the given project. This will be auto-assigned. Format is &#x60;projects/{project}/databases/{database}/backupSchedules/{backup_schedule}&#x60; |  [optional] [readonly] |
|**retention** | **String** | At what relative time in the future, compared to its creation time, the backup should be deleted, e.g. keep backups for 7 days. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp at which this backup schedule was most recently updated. When a backup schedule is first created, this is the same as create_time. |  [optional] [readonly] |
|**weeklyRecurrence** | [**GoogleFirestoreAdminV1WeeklyRecurrence**](GoogleFirestoreAdminV1WeeklyRecurrence.md) |  |  [optional] |



