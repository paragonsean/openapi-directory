# ThePlaidApi.BankTransferCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. | 
**accountId** | **String** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | 
**achClass** | [**ACHClass**](ACHClass.md) |  | [optional] 
**amount** | **String** | The amount of the bank transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**customTag** | **String** | An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters. | [optional] 
**description** | **String** | The transfer description. Maximum of 10 characters. | 
**idempotencyKey** | **String** | A random key provided by the client, per unique bank transfer. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a bank transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single bank transfer is created. | 
**isoCurrencyCode** | **String** | The currency of the transfer amount – should be set to \&quot;USD\&quot;. | 
**metadata** | **{String: String}** | The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of 50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters  | [optional] 
**network** | [**BankTransferNetwork**](BankTransferNetwork.md) |  | 
**originationAccountId** | **String** | Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**type** | [**BankTransferType**](BankTransferType.md) |  | 
**user** | [**BankTransferUser**](BankTransferUser.md) |  | 


