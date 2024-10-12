# CloudComposerApi.ScheduledSnapshotsConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Optional. Whether scheduled snapshots creation is enabled. | [optional] 
**snapshotCreationSchedule** | **String** | Optional. The cron expression representing the time when snapshots creation mechanism runs. This field is subject to additional validation around frequency of execution. | [optional] 
**snapshotLocation** | **String** | Optional. The Cloud Storage location for storing automatically created snapshots. | [optional] 
**timeZone** | **String** | Optional. Time zone that sets the context to interpret snapshot_creation_schedule. | [optional] 


