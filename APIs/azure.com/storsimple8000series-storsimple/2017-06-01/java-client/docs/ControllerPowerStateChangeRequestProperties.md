

# ControllerPowerStateChangeRequestProperties

The properties of the controller power state change request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The power state that the request is expecting for the controller of the device. |  |
|**activeController** | [**ActiveControllerEnum**](#ActiveControllerEnum) | The active controller that the request is expecting on the device. |  |
|**controller0State** | [**Controller0StateEnum**](#Controller0StateEnum) | The controller 0&#39;s status that the request is expecting on the device. |  |
|**controller1State** | [**Controller1StateEnum**](#Controller1StateEnum) | The controller 1&#39;s status that the request is expecting on the device. |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| START | &quot;Start&quot; |
| RESTART | &quot;Restart&quot; |
| SHUTDOWN | &quot;Shutdown&quot; |



## Enum: ActiveControllerEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NONE | &quot;None&quot; |
| CONTROLLER0 | &quot;Controller0&quot; |
| CONTROLLER1 | &quot;Controller1&quot; |



## Enum: Controller0StateEnum

| Name | Value |
|---- | -----|
| NOT_PRESENT | &quot;NotPresent&quot; |
| POWERED_OFF | &quot;PoweredOff&quot; |
| OK | &quot;Ok&quot; |
| RECOVERING | &quot;Recovering&quot; |
| WARNING | &quot;Warning&quot; |
| FAILURE | &quot;Failure&quot; |



## Enum: Controller1StateEnum

| Name | Value |
|---- | -----|
| NOT_PRESENT | &quot;NotPresent&quot; |
| POWERED_OFF | &quot;PoweredOff&quot; |
| OK | &quot;Ok&quot; |
| RECOVERING | &quot;Recovering&quot; |
| WARNING | &quot;Warning&quot; |
| FAILURE | &quot;Failure&quot; |



