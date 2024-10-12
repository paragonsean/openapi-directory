# ThePlaidApi.TransferCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. Required if not using &#x60;payment_profile_token&#x60;. | [optional] 
**accountId** | **String** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. Returned only if &#x60;account_id&#x60; was set on intent creation. | [optional] 
**achClass** | [**ACHClass**](ACHClass.md) |  | [optional] 
**amount** | **String** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | [optional] 
**authorizationId** | **String** | Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier. | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**description** | **String** | The transfer description. Maximum of 10 characters. If reprocessing a returned transfer, please note that the &#x60;description&#x60; field must be &#x60;\&quot;Retry\&quot;&#x60; to indicate that it&#39;s a retry of a previously returned transfer. You may retry a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with code &#x60;R01&#x60; or &#x60;R09&#x60; may be retried. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes). | 
**idempotencyKey** | **String** | Deprecated. &#x60;authorization_id&#x60; is now used as idempotency instead.  A random key provided by the client, per unique transfer. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single transfer is created. | [optional] 
**isoCurrencyCode** | **String** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | [optional] 
**metadata** | **{String: String}** | The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of 50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters  | [optional] 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | [optional] 
**originationAccountId** | **String** | Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank. | [optional] 
**paymentProfileToken** | **String** | The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using &#x60;access_token&#x60;. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**type** | [**TransferType**](TransferType.md) |  | [optional] 
**user** | [**TransferUserInRequestDeprecated**](TransferUserInRequestDeprecated.md) |  | [optional] 


