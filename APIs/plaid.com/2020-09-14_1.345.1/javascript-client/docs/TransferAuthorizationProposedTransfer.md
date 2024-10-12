# ThePlaidApi.TransferAuthorizationProposedTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | [optional] 
**achClass** | [**ACHClass**](ACHClass.md) |  | [optional] 
**amount** | **String** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**fundingAccountId** | **String** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**isoCurrencyCode** | **String** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | 
**network** | **String** | The network or rails used for the transfer. | 
**originationAccountId** | **String** | Plaid&#39;s unique identifier for the origination account that was used for this transfer. | 
**originatorClientId** | **String** | The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS). | 
**type** | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 


