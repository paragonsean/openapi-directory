

# ClusterUpgradeUpgradeStatus

UpgradeStatus provides status information for each upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Status code of the upgrade. |  [optional] |
|**reason** | **String** | Reason for this status. |  [optional] |
|**updateTime** | **String** | Last timestamp the status was updated. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| INELIGIBLE | &quot;INELIGIBLE&quot; |
| PENDING | &quot;PENDING&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| SOAKING | &quot;SOAKING&quot; |
| FORCED_SOAKING | &quot;FORCED_SOAKING&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



