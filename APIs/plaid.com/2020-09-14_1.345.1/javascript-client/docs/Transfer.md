# ThePlaidApi.Transfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. | [optional] 
**achClass** | [**ACHClass**](ACHClass.md) |  | [optional] 
**amount** | **String** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**cancellable** | **Boolean** | When &#x60;true&#x60;, you can still cancel this transfer. | 
**created** | **Date** | The datetime when this transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | 
**description** | **String** | The description of the transfer. | 
**expectedSettlementDate** | **Date** | The expected date when the full amount of the transfer settles at the consumers’ account, if the transfer is credit; or at the customer&#39;s business checking account, if the transfer is debit. Only set for ACH transfers and is null for non-ACH transfers. Only set for ACH transfers. This will be of the form YYYY-MM-DD. | 
**expectedSettlementSchedule** | [**[TransferExpectedSettlementScheduleItem]**](TransferExpectedSettlementScheduleItem.md) | The expected settlement schedule of this transfer, if posted. Only applies to ACH debit transfers. | [optional] 
**failureReason** | [**TransferFailure**](TransferFailure.md) |  | 
**fundingAccountId** | **String** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**guaranteeDecision** | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) |  | 
**guaranteeDecisionRationale** | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) |  | 
**id** | **String** | Plaid’s unique identifier for a transfer. | 
**isoCurrencyCode** | **String** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**metadata** | **{String: String}** | The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of 50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters  | 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**originationAccountId** | **String** | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**originatorClientId** | **String** | The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS). | 
**recurringTransferId** | **String** | The id of the recurring transfer if this transfer belongs to a recurring transfer. | 
**refunds** | [**[TransferRefund]**](TransferRefund.md) | A list of refunds associated with this transfer. | 
**settledAmount** | **String** | The accumulated amount that have been swept to date. This number does not reflect &#x60;return_swept&#x60; amount if the transfer is returned. Only applies to ACH debit transfers. | [optional] 
**standardReturnWindow** | **Date** | The date 3 business days from settlement date indicating the following ACH returns can no longer happen: R01, R02, R03, R29. This will be of the form YYYY-MM-DD. | 
**status** | [**TransferStatus**](TransferStatus.md) |  | 
**sweepStatus** | [**TransferSweepStatus**](TransferSweepStatus.md) |  | [optional] 
**type** | [**TransferType**](TransferType.md) |  | 
**unauthorizedReturnWindow** | **Date** | The date 61 business days from settlement date indicating the following ACH returns can no longer happen: R05, R07, R10, R11, R51, R33, R37, R38, R51, R52, R53. This will be of the form YYYY-MM-DD. | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 


