

# PatientSMSNotifcationResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**Error**](Error.md) |  |  [optional] |
|**requestId** | **UUID** | a nonce, unique for each HTTP request |  |
|**resp** | [**RequestReference**](RequestReference.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACKNOWLEDGED | &quot;ACKNOWLEDGED&quot; |
| ERRORED | &quot;ERRORED&quot; |



