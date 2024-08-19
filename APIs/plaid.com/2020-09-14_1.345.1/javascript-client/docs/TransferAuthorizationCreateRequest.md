# ThePlaidApi.TransferAuthorizationCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. Required if not using &#x60;payment_profile_token&#x60;. | [optional] 
**accountId** | **String** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. Returned only if &#x60;account_id&#x60; was set on intent creation. | [optional] 
**achClass** | [**ACHClass**](ACHClass.md) |  | [optional] 
**amount** | **String** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**beaconSessionId** | **String** | The unique identifier returned by Plaid&#39;s [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage. Required for Guarantee customers who are not using [Transfer UI](https://plaid.com/docs/transfer/using-transfer-ui/) and have a web checkout experience. | [optional] 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**device** | [**TransferAuthorizationDevice**](TransferAuthorizationDevice.md) |  | [optional] 
**fundingAccountId** | **String** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. Defaults to the account configured during onboarding. | [optional] 
**idempotencyKey** | **String** | A random key provided by the client, per unique authorization. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create an authorization fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single authorization is created.  Failure to provide this key may result in duplicate charges.  Required for guaranteed ACH customers. | [optional] 
**isoCurrencyCode** | **String** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | [optional] 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**originationAccountId** | **String** | Plaid&#39;s unique identifier for the origination account for this authorization. If not specified, the default account will be used. | [optional] 
**originatorClientId** | **String** | The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a third-party sender (TPS). | [optional] 
**paymentProfileToken** | **String** | The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using &#x60;access_token&#x60;. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**type** | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferAuthorizationUserInRequest**](TransferAuthorizationUserInRequest.md) |  | 
**userPresent** | **Boolean** | Required for Guarantee. If the end user is initiating the specific transfer themselves via an interactive UI, this should be &#x60;true&#x60;; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be &#x60;false&#x60;. | [optional] 
**withGuarantee** | **Boolean** | If set to &#x60;false&#x60;, Plaid will not offer a &#x60;guarantee_decision&#x60; for this request(Guarantee customers only). | [optional] [default to true]


