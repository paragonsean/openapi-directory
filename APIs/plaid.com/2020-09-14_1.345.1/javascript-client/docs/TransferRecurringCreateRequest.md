# ThePlaidApi.TransferRecurringCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. Required if not using &#x60;payment_profile_token&#x60;. | 
**accountId** | **String** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. Returned only if &#x60;account_id&#x60; was set on intent creation. | 
**achClass** | [**ACHClass**](ACHClass.md) |  | [optional] 
**amount** | **String** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**description** | **String** | The description of the recurring transfer. | 
**device** | [**TransferDevice**](TransferDevice.md) |  | 
**fundingAccountId** | **String** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. Defaults to the account configured during onboarding. | [optional] 
**idempotencyKey** | **String** | A random key provided by the client, per unique recurring transfer. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a recurring fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single recurring transfer is created. | 
**isoCurrencyCode** | **String** | The currency of the transfer amount. The default value is \&quot;USD\&quot;. | [optional] 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**schedule** | [**TransferRecurringSchedule**](TransferRecurringSchedule.md) |  | 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**testClockId** | **String** | Plaid’s unique identifier for a test clock. | [optional] 
**type** | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferUserInRequest**](TransferUserInRequest.md) |  | 
**userPresent** | **Boolean** | If the end user is initiating the specific transfer themselves via an interactive UI, this should be &#x60;true&#x60;; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be &#x60;false&#x60;. | 


