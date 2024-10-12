# SqlManagementClient.AutomaticTuningOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualState** | **String** | Automatic tuning option actual state. | [optional] [readonly] 
**desiredState** | **String** | Automatic tuning option desired state. | [optional] 
**reasonCode** | **Number** | Reason code if desired and actual state are different. | [optional] [readonly] 
**reasonDesc** | **String** | Reason description if desired and actual state are different. | [optional] [readonly] 



## Enum: ActualStateEnum


* `Off` (value: `"Off"`)

* `On` (value: `"On"`)





## Enum: DesiredStateEnum


* `Off` (value: `"Off"`)

* `On` (value: `"On"`)

* `Default` (value: `"Default"`)





## Enum: ReasonDescEnum


* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)

* `AutoConfigured` (value: `"AutoConfigured"`)

* `InheritedFromServer` (value: `"InheritedFromServer"`)

* `QueryStoreOff` (value: `"QueryStoreOff"`)

* `QueryStoreReadOnly` (value: `"QueryStoreReadOnly"`)

* `NotSupported` (value: `"NotSupported"`)




