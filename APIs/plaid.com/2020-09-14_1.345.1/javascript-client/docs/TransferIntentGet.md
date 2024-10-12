# ThePlaidApi.TransferIntentGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. Returned only if &#x60;account_id&#x60; was set on intent creation. | [optional] 
**achClass** | [**ACHClass**](ACHClass.md) |  | [optional] 
**amount** | **String** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**authorizationDecision** | [**TransferIntentAuthorizationDecision**](TransferIntentAuthorizationDecision.md) |  | 
**authorizationDecisionRationale** | [**TransferAuthorizationDecisionRationale**](TransferAuthorizationDecisionRationale.md) |  | 
**created** | **Date** | The datetime the transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | 
**description** | **String** | A description for the underlying transfer. Maximum of 8 characters. | 
**failureReason** | [**TransferIntentGetFailureReason**](TransferIntentGetFailureReason.md) |  | 
**fundingAccountId** | **String** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**guaranteeDecision** | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) |  | 
**guaranteeDecisionRationale** | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) |  | 
**id** | **String** | Plaid&#39;s unique identifier for a transfer intent object. | 
**isoCurrencyCode** | **String** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**metadata** | **{String: String}** | The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of 50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters  | [optional] 
**mode** | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) |  | 
**network** | [**TransferIntentCreateNetwork**](TransferIntentCreateNetwork.md) |  | [optional] 
**originationAccountId** | **String** | Plaid’s unique identifier for the origination account used for the transfer. | 
**requireGuarantee** | **Boolean** | When &#x60;true&#x60;, the transfer requires a &#x60;GUARANTEED&#x60; decision by Plaid to proceed (Guarantee customers only). | [optional] 
**status** | [**TransferIntentStatus**](TransferIntentStatus.md) |  | 
**transferId** | **String** | Plaid&#39;s unique identifier for the transfer created through the UI. Returned only if the transfer was successfully created. Null value otherwise. | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 


