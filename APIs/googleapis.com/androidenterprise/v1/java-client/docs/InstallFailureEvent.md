

# InstallFailureEvent

An event generated when an app installation failed on a device

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceId** | **String** | The Android ID of the device. This field will always be present. |  [optional] |
|**failureDetails** | **String** | Additional details on the failure if applicable. |  [optional] |
|**failureReason** | [**FailureReasonEnum**](#FailureReasonEnum) | The reason for the installation failure. This field will always be present. |  [optional] |
|**productId** | **String** | The id of the product (e.g. \&quot;app:com.google.android.gm\&quot;) for which the install failure event occured. This field will always be present. |  [optional] |
|**userId** | **String** | The ID of the user. This field will always be present. |  [optional] |



## Enum: FailureReasonEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| TIMEOUT | &quot;timeout&quot; |



