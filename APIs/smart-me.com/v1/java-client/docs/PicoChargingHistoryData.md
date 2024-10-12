

# PicoChargingHistoryData

Api container for the charging station history

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **Integer** | The duration in seconds |  [optional] [readonly] |
|**energyUsed** | **Double** | The energy used (in kWh) |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The starttime of the charging (in UTC) |  [optional] [readonly] |
|**transactionStopReason** | [**TransactionStopReasonEnum**](#TransactionStopReasonEnum) |  |  [optional] [readonly] |



## Enum: TransactionStopReasonEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CAR_DISCONNECTED | &quot;CarDisconnected&quot; |
| REMOTE_STOP | &quot;RemoteStop&quot; |
| ERROR_STOP | &quot;ErrorStop&quot; |
| INSTALLATION_MODE | &quot;InstallationMode&quot; |
| CABLE_ERROR | &quot;CableError&quot; |
| DIODE_ERROR | &quot;DiodeError&quot; |
| RCD_ERROR | &quot;RcdError&quot; |
| OVERLOAD_ERROR | &quot;OverloadError&quot; |



