

# PersistenceConfig

Configuration of the persistence functionality.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**persistenceMode** | [**PersistenceModeEnum**](#PersistenceModeEnum) | Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used. |  [optional] |
|**rdbNextSnapshotTime** | **String** | Output only. The next time that a snapshot attempt is scheduled to occur. |  [optional] [readonly] |
|**rdbSnapshotPeriod** | [**RdbSnapshotPeriodEnum**](#RdbSnapshotPeriodEnum) | Optional. Period between RDB snapshots. Snapshots will be attempted every period starting from the provided snapshot start time. For example, a start time of 01/01/2033 06:45 and SIX_HOURS snapshot period will do nothing until 01/01/2033, and then trigger snapshots every day at 06:45, 12:45, 18:45, and 00:45 the next day, and so on. If not provided, TWENTY_FOUR_HOURS will be used as default. |  [optional] |
|**rdbSnapshotStartTime** | **String** | Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used. |  [optional] |



## Enum: PersistenceModeEnum

| Name | Value |
|---- | -----|
| PERSISTENCE_MODE_UNSPECIFIED | &quot;PERSISTENCE_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| RDB | &quot;RDB&quot; |



## Enum: RdbSnapshotPeriodEnum

| Name | Value |
|---- | -----|
| SNAPSHOT_PERIOD_UNSPECIFIED | &quot;SNAPSHOT_PERIOD_UNSPECIFIED&quot; |
| ONE_HOUR | &quot;ONE_HOUR&quot; |
| SIX_HOURS | &quot;SIX_HOURS&quot; |
| TWELVE_HOURS | &quot;TWELVE_HOURS&quot; |
| TWENTY_FOUR_HOURS | &quot;TWENTY_FOUR_HOURS&quot; |



