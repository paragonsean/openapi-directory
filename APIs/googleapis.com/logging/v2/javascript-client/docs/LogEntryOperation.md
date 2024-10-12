# CloudLoggingApi.LogEntryOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **Boolean** | Optional. Set this to True if this is the first log entry in the operation. | [optional] 
**id** | **String** | Optional. An arbitrary operation identifier. Log entries with the same identifier are assumed to be part of the same operation. | [optional] 
**last** | **Boolean** | Optional. Set this to True if this is the last log entry in the operation. | [optional] 
**producer** | **String** | Optional. An arbitrary producer identifier. The combination of id and producer must be globally unique. Examples for producer: \&quot;MyDivision.MyBigCompany.com\&quot;, \&quot;github.com/MyProject/MyApplication\&quot;. | [optional] 


