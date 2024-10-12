

# ContinuousBackupInfo

ContinuousBackupInfo describes the continuous backup properties of a cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**earliestRestorableTime** | **String** | Output only. The earliest restorable time that can be restored to. Output only field. |  [optional] [readonly] |
|**enabledTime** | **String** | Output only. When ContinuousBackup was most recently enabled. Set to null if ContinuousBackup is not enabled. |  [optional] [readonly] |
|**encryptionInfo** | [**EncryptionInfo**](EncryptionInfo.md) |  |  [optional] |
|**schedule** | [**List&lt;ScheduleEnum&gt;**](#List&lt;ScheduleEnum&gt;) | Output only. Days of the week on which a continuous backup is taken. Output only field. Ignored if passed into the request. |  [optional] [readonly] |



## Enum: List&lt;ScheduleEnum&gt;

| Name | Value |
|---- | -----|
| DAY_OF_WEEK_UNSPECIFIED | &quot;DAY_OF_WEEK_UNSPECIFIED&quot; |
| MONDAY | &quot;MONDAY&quot; |
| TUESDAY | &quot;TUESDAY&quot; |
| WEDNESDAY | &quot;WEDNESDAY&quot; |
| THURSDAY | &quot;THURSDAY&quot; |
| FRIDAY | &quot;FRIDAY&quot; |
| SATURDAY | &quot;SATURDAY&quot; |
| SUNDAY | &quot;SUNDAY&quot; |



