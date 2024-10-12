# PayRunIo.CisTransaction1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cisMessageType** | **String** | The cis transactions&#39; cis message type | [optional] 
**employerCore** | [**EmployerCore**](EmployerCore.md) |  | [optional] 
**requestData** | **String** | The cis transactions&#39; request data | [optional] 
**responseData** | **String** | The cis transactions&#39; response data | [optional] 
**taxYear** | **Number** | The cis transactions&#39; tax year | [optional] 
**timestamp** | **Date** | The cis transactions&#39; timestamp | [optional] 
**transactionStatus** | **String** | The cis transactions&#39; transaction status | [optional] 
**transmissionDate** | **Date** | The cis transactions&#39; transmission date | [optional] 



## Enum: CisMessageTypeEnum


* `Verification` (value: `"Verification"`)

* `Return` (value: `"Return"`)





## Enum: TransactionStatusEnum


* `New` (value: `"New"`)

* `RequestGenerated` (value: `"RequestGenerated"`)

* `CompletedWithError` (value: `"CompletedWithError"`)

* `CompletedWithSuccess` (value: `"CompletedWithSuccess"`)

* `TimeOut` (value: `"TimeOut"`)




