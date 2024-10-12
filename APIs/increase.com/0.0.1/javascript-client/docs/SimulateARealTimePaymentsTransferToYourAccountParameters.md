# IncreaseApi.SimulateARealTimePaymentsTransferToYourAccountParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumberId** | **String** | The identifier of the Account Number the inbound Real Time Payments Transfer is for. | 
**amount** | **Number** | The transfer amount in USD cents. Must be positive. | 
**debtorAccountNumber** | **String** | The account number of the account that sent the transfer. | [optional] 
**debtorName** | **String** | The name provided by the sender of the transfer. | [optional] 
**debtorRoutingNumber** | **String** | The routing number of the account that sent the transfer. | [optional] 
**remittanceInformation** | **String** | Additional information included with the transfer. | [optional] 
**requestForPaymentId** | **String** | The identifier of a pending Request for Payment that this transfer will fulfill. | [optional] 


