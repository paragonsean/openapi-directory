# GoogleCloudMemorystoreForRedisApi.PersistenceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persistenceMode** | **String** | Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used. | [optional] 
**rdbNextSnapshotTime** | **String** | Output only. The next time that a snapshot attempt is scheduled to occur. | [optional] [readonly] 
**rdbSnapshotPeriod** | **String** | Optional. Period between RDB snapshots. Snapshots will be attempted every period starting from the provided snapshot start time. For example, a start time of 01/01/2033 06:45 and SIX_HOURS snapshot period will do nothing until 01/01/2033, and then trigger snapshots every day at 06:45, 12:45, 18:45, and 00:45 the next day, and so on. If not provided, TWENTY_FOUR_HOURS will be used as default. | [optional] 
**rdbSnapshotStartTime** | **String** | Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used. | [optional] 



## Enum: PersistenceModeEnum


* `PERSISTENCE_MODE_UNSPECIFIED` (value: `"PERSISTENCE_MODE_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `RDB` (value: `"RDB"`)





## Enum: RdbSnapshotPeriodEnum


* `SNAPSHOT_PERIOD_UNSPECIFIED` (value: `"SNAPSHOT_PERIOD_UNSPECIFIED"`)

* `ONE_HOUR` (value: `"ONE_HOUR"`)

* `SIX_HOURS` (value: `"SIX_HOURS"`)

* `TWELVE_HOURS` (value: `"TWELVE_HOURS"`)

* `TWENTY_FOUR_HOURS` (value: `"TWENTY_FOUR_HOURS"`)




