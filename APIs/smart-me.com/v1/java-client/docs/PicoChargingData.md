

# PicoChargingData

Container class for the pico charging station API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeChargingEnergy** | **Double** | The energy used by this active charging (in kWh) |  [optional] |
|**activeChargingPower** | **Double** | The power of the active charging (in kW) |  [optional] |
|**connectionMode** | [**ConnectionModeEnum**](#ConnectionModeEnum) | The mode how this station is connected to the cloud |  [optional] |
|**duration** | **Integer** | The duration of this charging in seconds |  [optional] |
|**lastWarningOrError** | [**LastWarningOrErrorEnum**](#LastWarningOrErrorEnum) | The last warning or error of the station. This message is only shown if the warning or error happend in the last 5 minutes. |  [optional] |
|**lastWarningOrErrorMessage** | **String** | The message of the last warning or error of the station. |  [optional] |
|**lastWarningOrErrorTime** | **OffsetDateTime** | The time when the LastWarningOrError happend |  [optional] |
|**loadSheddingState** | [**LoadSheddingStateEnum**](#LoadSheddingStateEnum) | Max. dynamic current (e.g. set over API or Modbus TCP) of this station or the loadmanagement group of the station if the station is in a group. in A |  [optional] |
|**loadmanagementGroupName** | **String** | The name of the loadmanagement group. Or string.empty if the station is not in a group |  [optional] |
|**maxAllowedChargingCurrent** | **Integer** | Max allowed charging current in A |  [optional] |
|**maxDynamicCurrent** | **Integer** | Max. dynamic current (e.g. set over API or Modbus TCP) of this station or the loadmanagement group of the station if the station is in a group. in A |  [optional] |
|**maxLoadmanagementGroupCurrent** | **Integer** | Max. current of the loadmanagement group of this station (if there is any) in A |  [optional] |
|**maxStationCurrent** | **Integer** | Max. current of the station in A |  [optional] |
|**minStationCurrent** | **Integer** | Min. current of the station in A |  [optional] |
|**RSSI** | **Integer** | Received Signal Strength Indicator for the connection mode (wifi or mobile).               -127 (min) to 0 (Max) |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the charging station |  [optional] [readonly] |
|**valueDate** | **OffsetDateTime** | The date of this values |  [optional] |



## Enum: ConnectionModeEnum

| Name | Value |
|---- | -----|
| NO_CONNECTION | &quot;NetworkToCloudConnectionMode_NoConnection&quot; |
| DIRECT_WI_FI_CONNECTION | &quot;NetworkToCloudConnectionMode_DirectWiFiConnection&quot; |
| GPRS_CONNECTION | &quot;NetworkToCloudConnectionMode_GPRSConnection&quot; |
| NB_IOT_CONNECTION | &quot;NetworkToCloudConnectionMode_NBIotConnection&quot; |
| LTE_CAT_M1_CONNECTION | &quot;NetworkToCloudConnectionMode_LteCatM1Connection&quot; |
| MESH_WI_FI_CONNECTION | &quot;NetworkToCloudConnectionMode_MeshWiFiConnection&quot; |
| MESH_MOBILE_CONNECTION | &quot;NetworkToCloudConnectionMode_MeshMobileConnection&quot; |



## Enum: LastWarningOrErrorEnum

| Name | Value |
|---- | -----|
| METER_DATALOGGER_EVENT | &quot;MeterDataloggerEvent&quot; |
| METER_RESTART | &quot;MeterRestart&quot; |
| POWER_DOWN | &quot;PowerDown&quot; |
| MISSING_PHASE_L1 | &quot;MissingPhaseL1&quot; |
| MISSING_PHASE_L2 | &quot;MissingPhaseL2&quot; |
| MISSING_PHASE_L3 | &quot;MissingPhaseL3&quot; |
| TAMPER_DETECTION_COVER | &quot;TamperDetectionCover&quot; |
| MAGNETIC_FIELD_DETECTION | &quot;MagneticFieldDetection&quot; |
| CLOCK_ADJUSTED | &quot;ClockAdjusted&quot; |
| OVERVOLTAGE | &quot;Overvoltage&quot; |
| UNDERVOLTAGE | &quot;Undervoltage&quot; |
| OVERVOLTAGE_L1 | &quot;OvervoltageL1&quot; |
| OVERVOLTAGE_L2 | &quot;OvervoltageL2&quot; |
| OVERVOLTAGE_L3 | &quot;OvervoltageL3&quot; |
| CHARGING_TRANSACTION | &quot;ChargingTransaction&quot; |
| PICO_ERROR_CONTROLLER_PANIC | &quot;PicoErrorControllerPanic&quot; |
| PICO_ERROR_MID_SERVICE_PANIC | &quot;PicoErrorMidServicePanic&quot; |
| PICO_WARNING_RCD_TRIGGERED | &quot;PicoWarningRcdTriggered&quot; |
| PICO_WARNING_CABLE_LOCK_ERROR | &quot;PicoWarningCableLockError&quot; |
| PICO_WARNING_DIODE_FAILURE | &quot;PicoWarningDiodeFailure&quot; |
| PICO_WARNING_OVERLOAD | &quot;PicoWarningOverload&quot; |
| PICO_WARNING_HIGH_TEMPERATURE | &quot;PicoWarningHighTemperature&quot; |



## Enum: LoadSheddingStateEnum

| Name | Value |
|---- | -----|
| MAX_CURRENT | &quot;MaxCurrent&quot; |
| HALF_CURRENT | &quot;HalfCurrent&quot; |
| MIN_CURRENT | &quot;MinCurrent&quot; |
| NO_CURRENT | &quot;NoCurrent&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| BOOTING | &quot;Booting&quot; |
| READY_NO_CAR_CONNECTED | &quot;ReadyNoCarConnected&quot; |
| READY_CAR_CONNECTED | &quot;ReadyCarConnected&quot; |
| STARTED_WAIT_FOR_CAR | &quot;StartedWaitForCar&quot; |
| CHARGING | &quot;Charging&quot; |
| INSTALLATION | &quot;Installation&quot; |
| AUTHORIZE | &quot;Authorize&quot; |
| OFFLINE | &quot;Offline&quot; |



