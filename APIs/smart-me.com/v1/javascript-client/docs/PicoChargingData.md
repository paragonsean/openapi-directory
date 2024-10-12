# SmartMe.PicoChargingData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeChargingEnergy** | **Number** | The energy used by this active charging (in kWh) | [optional] 
**activeChargingPower** | **Number** | The power of the active charging (in kW) | [optional] 
**connectionMode** | **String** | The mode how this station is connected to the cloud | [optional] 
**duration** | **Number** | The duration of this charging in seconds | [optional] 
**lastWarningOrError** | **String** | The last warning or error of the station. This message is only shown if the warning or error happend in the last 5 minutes. | [optional] 
**lastWarningOrErrorMessage** | **String** | The message of the last warning or error of the station. | [optional] 
**lastWarningOrErrorTime** | **Date** | The time when the LastWarningOrError happend | [optional] 
**loadSheddingState** | **String** | Max. dynamic current (e.g. set over API or Modbus TCP) of this station or the loadmanagement group of the station if the station is in a group. in A | [optional] 
**loadmanagementGroupName** | **String** | The name of the loadmanagement group. Or string.empty if the station is not in a group | [optional] 
**maxAllowedChargingCurrent** | **Number** | Max allowed charging current in A | [optional] 
**maxDynamicCurrent** | **Number** | Max. dynamic current (e.g. set over API or Modbus TCP) of this station or the loadmanagement group of the station if the station is in a group. in A | [optional] 
**maxLoadmanagementGroupCurrent** | **Number** | Max. current of the loadmanagement group of this station (if there is any) in A | [optional] 
**maxStationCurrent** | **Number** | Max. current of the station in A | [optional] 
**minStationCurrent** | **Number** | Min. current of the station in A | [optional] 
**RSSI** | **Number** | Received Signal Strength Indicator for the connection mode (wifi or mobile).               -127 (min) to 0 (Max) | [optional] 
**state** | **String** | The state of the charging station | [optional] [readonly] 
**valueDate** | **Date** | The date of this values | [optional] 



## Enum: ConnectionModeEnum


* `NoConnection` (value: `"NetworkToCloudConnectionMode_NoConnection"`)

* `DirectWiFiConnection` (value: `"NetworkToCloudConnectionMode_DirectWiFiConnection"`)

* `GPRSConnection` (value: `"NetworkToCloudConnectionMode_GPRSConnection"`)

* `NBIotConnection` (value: `"NetworkToCloudConnectionMode_NBIotConnection"`)

* `LteCatM1Connection` (value: `"NetworkToCloudConnectionMode_LteCatM1Connection"`)

* `MeshWiFiConnection` (value: `"NetworkToCloudConnectionMode_MeshWiFiConnection"`)

* `MeshMobileConnection` (value: `"NetworkToCloudConnectionMode_MeshMobileConnection"`)





## Enum: LastWarningOrErrorEnum


* `MeterDataloggerEvent` (value: `"MeterDataloggerEvent"`)

* `MeterRestart` (value: `"MeterRestart"`)

* `PowerDown` (value: `"PowerDown"`)

* `MissingPhaseL1` (value: `"MissingPhaseL1"`)

* `MissingPhaseL2` (value: `"MissingPhaseL2"`)

* `MissingPhaseL3` (value: `"MissingPhaseL3"`)

* `TamperDetectionCover` (value: `"TamperDetectionCover"`)

* `MagneticFieldDetection` (value: `"MagneticFieldDetection"`)

* `ClockAdjusted` (value: `"ClockAdjusted"`)

* `Overvoltage` (value: `"Overvoltage"`)

* `Undervoltage` (value: `"Undervoltage"`)

* `OvervoltageL1` (value: `"OvervoltageL1"`)

* `OvervoltageL2` (value: `"OvervoltageL2"`)

* `OvervoltageL3` (value: `"OvervoltageL3"`)

* `ChargingTransaction` (value: `"ChargingTransaction"`)

* `PicoErrorControllerPanic` (value: `"PicoErrorControllerPanic"`)

* `PicoErrorMidServicePanic` (value: `"PicoErrorMidServicePanic"`)

* `PicoWarningRcdTriggered` (value: `"PicoWarningRcdTriggered"`)

* `PicoWarningCableLockError` (value: `"PicoWarningCableLockError"`)

* `PicoWarningDiodeFailure` (value: `"PicoWarningDiodeFailure"`)

* `PicoWarningOverload` (value: `"PicoWarningOverload"`)

* `PicoWarningHighTemperature` (value: `"PicoWarningHighTemperature"`)





## Enum: LoadSheddingStateEnum


* `MaxCurrent` (value: `"MaxCurrent"`)

* `HalfCurrent` (value: `"HalfCurrent"`)

* `MinCurrent` (value: `"MinCurrent"`)

* `NoCurrent` (value: `"NoCurrent"`)





## Enum: StateEnum


* `Booting` (value: `"Booting"`)

* `ReadyNoCarConnected` (value: `"ReadyNoCarConnected"`)

* `ReadyCarConnected` (value: `"ReadyCarConnected"`)

* `StartedWaitForCar` (value: `"StartedWaitForCar"`)

* `Charging` (value: `"Charging"`)

* `Installation` (value: `"Installation"`)

* `Authorize` (value: `"Authorize"`)

* `Offline` (value: `"Offline"`)




