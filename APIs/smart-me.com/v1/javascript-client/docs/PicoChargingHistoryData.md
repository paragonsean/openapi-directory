# SmartMe.PicoChargingHistoryData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **Number** | The duration in seconds | [optional] [readonly] 
**energyUsed** | **Number** | The energy used (in kWh) | [optional] [readonly] 
**startTime** | **Date** | The starttime of the charging (in UTC) | [optional] [readonly] 
**transactionStopReason** | **String** |  | [optional] [readonly] 



## Enum: TransactionStopReasonEnum


* `Unknown` (value: `"Unknown"`)

* `CarDisconnected` (value: `"CarDisconnected"`)

* `RemoteStop` (value: `"RemoteStop"`)

* `ErrorStop` (value: `"ErrorStop"`)

* `InstallationMode` (value: `"InstallationMode"`)

* `CableError` (value: `"CableError"`)

* `DiodeError` (value: `"DiodeError"`)

* `RcdError` (value: `"RcdError"`)

* `OverloadError` (value: `"OverloadError"`)




