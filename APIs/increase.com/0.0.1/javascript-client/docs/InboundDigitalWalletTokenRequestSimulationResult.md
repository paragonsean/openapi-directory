# IncreaseApi.InboundDigitalWalletTokenRequestSimulationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**declineReason** | **String** | If the simulated tokenization attempt was declined, this field contains details as to why. | 
**digitalWalletTokenId** | **String** | If the simulated tokenization attempt was accepted, this field contains the id of the Digital Wallet Token that was created. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;inbound_digital_wallet_token_request_simulation_result&#x60;. | 



## Enum: DeclineReasonEnum


* `card_not_active` (value: `"card_not_active"`)

* `no_verification_method` (value: `"no_verification_method"`)

* `webhook_timed_out` (value: `"webhook_timed_out"`)

* `webhook_declined` (value: `"webhook_declined"`)





## Enum: TypeEnum


* `inbound_digital_wallet_token_request_simulation_result` (value: `"inbound_digital_wallet_token_request_simulation_result"`)




