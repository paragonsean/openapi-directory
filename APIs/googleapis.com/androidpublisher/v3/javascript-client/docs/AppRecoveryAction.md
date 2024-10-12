# GooglePlayAndroidDeveloperApi.AppRecoveryAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appRecoveryId** | **String** | ID corresponding to the app recovery action. | [optional] 
**cancelTime** | **String** | Timestamp of when the app recovery action is canceled by the developer. Only set if the recovery action has been canceled. | [optional] 
**createTime** | **String** | Timestamp of when the app recovery action is created by the developer. It is always set after creation of the recovery action. | [optional] 
**deployTime** | **String** | Timestamp of when the app recovery action is deployed to the users. Only set if the recovery action has been deployed. | [optional] 
**lastUpdateTime** | **String** | Timestamp of when the developer last updated recovery action. In case the action is cancelled, it corresponds to cancellation time. It is always set after creation of the recovery action. | [optional] 
**remoteInAppUpdateData** | [**RemoteInAppUpdateData**](RemoteInAppUpdateData.md) |  | [optional] 
**status** | **String** | The status of the recovery action. | [optional] 
**targeting** | [**Targeting**](Targeting.md) |  | [optional] 



## Enum: StatusEnum


* `UNSPECIFIED` (value: `"RECOVERY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"RECOVERY_STATUS_ACTIVE"`)

* `CANCELED` (value: `"RECOVERY_STATUS_CANCELED"`)

* `DRAFT` (value: `"RECOVERY_STATUS_DRAFT"`)

* `GENERATION_IN_PROGRESS` (value: `"RECOVERY_STATUS_GENERATION_IN_PROGRESS"`)

* `GENERATION_FAILED` (value: `"RECOVERY_STATUS_GENERATION_FAILED"`)




