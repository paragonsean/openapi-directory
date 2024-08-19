# IncreaseApi.CreateAWireTransferParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The identifier for the account that will send the transfer. | 
**accountNumber** | **String** | The account number for the destination account. | [optional] 
**amount** | **Number** | The transfer amount in cents. | 
**beneficiaryAddressLine1** | **String** | The beneficiary&#39;s address line 1. | [optional] 
**beneficiaryAddressLine2** | **String** | The beneficiary&#39;s address line 2. | [optional] 
**beneficiaryAddressLine3** | **String** | The beneficiary&#39;s address line 3. | [optional] 
**beneficiaryName** | **String** | The beneficiary&#39;s name. | 
**externalAccountId** | **String** | The ID of an External Account to initiate a transfer to. If this parameter is provided, &#x60;account_number&#x60; and &#x60;routing_number&#x60; must be absent. | [optional] 
**messageToRecipient** | **String** | The message that will show on the recipient&#39;s bank statement. | 
**requireApproval** | **Boolean** | Whether the transfer requires explicit approval via the dashboard or API. | [optional] 
**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN) for the destination account. | [optional] 


