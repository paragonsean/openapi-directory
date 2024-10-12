

# UpgradeDetails

Details for upgrading vault.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTimeUtc** | **OffsetDateTime** | UTC time at which the upgrade operation has ended. |  [optional] [readonly] |
|**lastUpdatedTimeUtc** | **OffsetDateTime** | UTC time at which the upgrade operation status was last updated. |  [optional] [readonly] |
|**message** | **String** | Message to the user containing information about the upgrade operation. |  [optional] [readonly] |
|**operationId** | **String** | ID of the vault upgrade operation. |  [optional] [readonly] |
|**previousResourceId** | **String** | Resource ID of the vault before the upgrade. |  [optional] [readonly] |
|**startTimeUtc** | **OffsetDateTime** | UTC time at which the upgrade operation has started. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the vault upgrade operation. |  [optional] [readonly] |
|**triggerType** | [**TriggerTypeEnum**](#TriggerTypeEnum) | The way the vault upgrade was triggered. |  [optional] [readonly] |
|**upgradedResourceId** | **String** | Resource ID of the upgraded vault. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| UPGRADED | &quot;Upgraded&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: TriggerTypeEnum

| Name | Value |
|---- | -----|
| USER_TRIGGERED | &quot;UserTriggered&quot; |
| FORCED_UPGRADE | &quot;ForcedUpgrade&quot; |



