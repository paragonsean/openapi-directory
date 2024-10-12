# StorSimple8000SeriesManagementClient.ControllerPowerStateChangeRequestProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The power state that the request is expecting for the controller of the device. | 
**activeController** | **String** | The active controller that the request is expecting on the device. | 
**controller0State** | **String** | The controller 0&#39;s status that the request is expecting on the device. | 
**controller1State** | **String** | The controller 1&#39;s status that the request is expecting on the device. | 



## Enum: ActionEnum


* `Start` (value: `"Start"`)

* `Restart` (value: `"Restart"`)

* `Shutdown` (value: `"Shutdown"`)





## Enum: ActiveControllerEnum


* `Unknown` (value: `"Unknown"`)

* `None` (value: `"None"`)

* `Controller0` (value: `"Controller0"`)

* `Controller1` (value: `"Controller1"`)





## Enum: Controller0StateEnum


* `NotPresent` (value: `"NotPresent"`)

* `PoweredOff` (value: `"PoweredOff"`)

* `Ok` (value: `"Ok"`)

* `Recovering` (value: `"Recovering"`)

* `Warning` (value: `"Warning"`)

* `Failure` (value: `"Failure"`)





## Enum: Controller1StateEnum


* `NotPresent` (value: `"NotPresent"`)

* `PoweredOff` (value: `"PoweredOff"`)

* `Ok` (value: `"Ok"`)

* `Recovering` (value: `"Recovering"`)

* `Warning` (value: `"Warning"`)

* `Failure` (value: `"Failure"`)




