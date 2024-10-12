

# AppRecoveryAction

Information about an app recovery action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appRecoveryId** | **String** | ID corresponding to the app recovery action. |  [optional] |
|**cancelTime** | **String** | Timestamp of when the app recovery action is canceled by the developer. Only set if the recovery action has been canceled. |  [optional] |
|**createTime** | **String** | Timestamp of when the app recovery action is created by the developer. It is always set after creation of the recovery action. |  [optional] |
|**deployTime** | **String** | Timestamp of when the app recovery action is deployed to the users. Only set if the recovery action has been deployed. |  [optional] |
|**lastUpdateTime** | **String** | Timestamp of when the developer last updated recovery action. In case the action is cancelled, it corresponds to cancellation time. It is always set after creation of the recovery action. |  [optional] |
|**remoteInAppUpdateData** | [**RemoteInAppUpdateData**](RemoteInAppUpdateData.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the recovery action. |  [optional] |
|**targeting** | [**Targeting**](Targeting.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;RECOVERY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;RECOVERY_STATUS_ACTIVE&quot; |
| CANCELED | &quot;RECOVERY_STATUS_CANCELED&quot; |
| DRAFT | &quot;RECOVERY_STATUS_DRAFT&quot; |
| GENERATION_IN_PROGRESS | &quot;RECOVERY_STATUS_GENERATION_IN_PROGRESS&quot; |
| GENERATION_FAILED | &quot;RECOVERY_STATUS_GENERATION_FAILED&quot; |



