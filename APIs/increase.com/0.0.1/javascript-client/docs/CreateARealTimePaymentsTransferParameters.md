# IncreaseApi.CreateARealTimePaymentsTransferParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The transfer amount in USD cents. For Real Time Payments transfers, must be positive. | 
**creditorName** | **String** | The name of the transfer&#39;s recipient. | 
**destinationAccountNumber** | **String** | The destination account number. | [optional] 
**destinationRoutingNumber** | **String** | The destination American Bankers&#39; Association (ABA) Routing Transit Number (RTN). | [optional] 
**externalAccountId** | **String** | The ID of an External Account to initiate a transfer to. If this parameter is provided, &#x60;destination_account_number&#x60; and &#x60;destination_routing_number&#x60; must be absent. | [optional] 
**remittanceInformation** | **String** | Unstructured information that will show on the recipient&#39;s bank statement. | 
**requireApproval** | **Boolean** | Whether the transfer requires explicit approval via the dashboard or API. | [optional] 
**sourceAccountNumberId** | **String** | The identifier of the Account Number from which to send the transfer. | 


