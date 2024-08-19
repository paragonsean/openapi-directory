# ThePlaidApi.SimulatedTransferSweep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **String** | Signed decimal amount of the sweep as it appears on your sweep account ledger (e.g. \&quot;-10.00\&quot;)  If amount is not present, the sweep was net-settled to zero and outstanding debits and credits between the sweep account and Plaid are balanced. | 
**created** | **Date** | The datetime when the sweep occurred, in RFC 3339 format. | 
**fundingAccountId** | **String** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**id** | **String** | Identifier of the sweep. | 
**isoCurrencyCode** | **String** | The currency of the sweep, e.g. \&quot;USD\&quot;. | 
**settled** | **Date** | The date when the sweep settled, in the YYYY-MM-DD format. | 


