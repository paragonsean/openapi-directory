# AlloyDbApi.ContinuousBackupInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earliestRestorableTime** | **String** | Output only. The earliest restorable time that can be restored to. Output only field. | [optional] [readonly] 
**enabledTime** | **String** | Output only. When ContinuousBackup was most recently enabled. Set to null if ContinuousBackup is not enabled. | [optional] [readonly] 
**encryptionInfo** | [**EncryptionInfo**](EncryptionInfo.md) |  | [optional] 
**schedule** | **[String]** | Output only. Days of the week on which a continuous backup is taken. Output only field. Ignored if passed into the request. | [optional] [readonly] 



## Enum: [ScheduleEnum]


* `DAY_OF_WEEK_UNSPECIFIED` (value: `"DAY_OF_WEEK_UNSPECIFIED"`)

* `MONDAY` (value: `"MONDAY"`)

* `TUESDAY` (value: `"TUESDAY"`)

* `WEDNESDAY` (value: `"WEDNESDAY"`)

* `THURSDAY` (value: `"THURSDAY"`)

* `FRIDAY` (value: `"FRIDAY"`)

* `SATURDAY` (value: `"SATURDAY"`)

* `SUNDAY` (value: `"SUNDAY"`)




