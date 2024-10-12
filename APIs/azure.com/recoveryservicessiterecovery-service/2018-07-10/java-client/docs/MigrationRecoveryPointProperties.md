

# MigrationRecoveryPointProperties

Migration item recovery point properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recoveryPointTime** | **OffsetDateTime** | The recovery point time. |  [optional] [readonly] |
|**recoveryPointType** | [**RecoveryPointTypeEnum**](#RecoveryPointTypeEnum) | The recovery point type. |  [optional] [readonly] |



## Enum: RecoveryPointTypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| APPLICATION_CONSISTENT | &quot;ApplicationConsistent&quot; |
| CRASH_CONSISTENT | &quot;CrashConsistent&quot; |



