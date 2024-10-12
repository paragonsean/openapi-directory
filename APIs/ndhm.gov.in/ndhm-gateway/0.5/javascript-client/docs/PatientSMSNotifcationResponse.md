# Gateway.PatientSMSNotifcationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**requestId** | **String** | a nonce, unique for each HTTP request | 
**resp** | [**RequestReference**](RequestReference.md) |  | 
**status** | **String** |  | [optional] 
**timestamp** | **Date** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 



## Enum: StatusEnum


* `ACKNOWLEDGED` (value: `"ACKNOWLEDGED"`)

* `ERRORED` (value: `"ERRORED"`)




