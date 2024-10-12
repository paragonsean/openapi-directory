

# GeneratedRecoveryApk

Download metadata for an app recovery module.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downloadId** | **String** | Download ID, which uniquely identifies the APK to download. Should be supplied to &#x60;generatedapks.download&#x60; method. |  [optional] |
|**moduleName** | **String** | Name of the module which recovery apk belongs to. |  [optional] |
|**recoveryId** | **String** | ID of the recovery action. |  [optional] |
|**recoveryStatus** | [**RecoveryStatusEnum**](#RecoveryStatusEnum) | The status of the recovery action corresponding to the recovery apk. |  [optional] |



## Enum: RecoveryStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;RECOVERY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;RECOVERY_STATUS_ACTIVE&quot; |
| CANCELED | &quot;RECOVERY_STATUS_CANCELED&quot; |
| DRAFT | &quot;RECOVERY_STATUS_DRAFT&quot; |
| GENERATION_IN_PROGRESS | &quot;RECOVERY_STATUS_GENERATION_IN_PROGRESS&quot; |
| GENERATION_FAILED | &quot;RECOVERY_STATUS_GENERATION_FAILED&quot; |



