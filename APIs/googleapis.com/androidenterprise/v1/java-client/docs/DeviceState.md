

# DeviceState

The state of a user's device, as accessed by the getState and setState methods on device resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountState** | [**AccountStateEnum**](#AccountStateEnum) | The state of the Google account on the device. \&quot;enabled\&quot; indicates that the Google account on the device can be used to access Google services (including Google Play), while \&quot;disabled\&quot; means that it cannot. A new device is initially in the \&quot;disabled\&quot; state. |  [optional] |



## Enum: AccountStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



