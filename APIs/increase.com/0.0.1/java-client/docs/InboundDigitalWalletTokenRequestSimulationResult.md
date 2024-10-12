

# InboundDigitalWalletTokenRequestSimulationResult

The results of a Digital Wallet Token simulation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**declineReason** | [**DeclineReasonEnum**](#DeclineReasonEnum) | If the simulated tokenization attempt was declined, this field contains details as to why. |  |
|**digitalWalletTokenId** | **String** | If the simulated tokenization attempt was accepted, this field contains the id of the Digital Wallet Token that was created. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;inbound_digital_wallet_token_request_simulation_result&#x60;. |  |



## Enum: DeclineReasonEnum

| Name | Value |
|---- | -----|
| CARD_NOT_ACTIVE | &quot;card_not_active&quot; |
| NO_VERIFICATION_METHOD | &quot;no_verification_method&quot; |
| WEBHOOK_TIMED_OUT | &quot;webhook_timed_out&quot; |
| WEBHOOK_DECLINED | &quot;webhook_declined&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INBOUND_DIGITAL_WALLET_TOKEN_REQUEST_SIMULATION_RESULT | &quot;inbound_digital_wallet_token_request_simulation_result&quot; |



