

# RealTimeDecision

Real Time Decisions are created when your application needs to take action in real-time to some event such as a card authorization. Real time decisions are currently in beta; please contact support@increase.com if you're interested in trying them out!

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardAuthorization** | [**CardAuthorization1**](CardAuthorization1.md) |  |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of the Real-Time Decision. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Real-Time Decision was created. |  |
|**digitalWalletAuthentication** | [**DigitalWalletAuthentication**](DigitalWalletAuthentication.md) |  |  |
|**digitalWalletToken** | [**DigitalWalletToken**](DigitalWalletToken.md) |  |  |
|**id** | **String** | The Real-Time Decision identifier. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the Real-Time Decision. |  |
|**timeoutAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which your application can no longer respond to the Real-Time Decision. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;real_time_decision&#x60;. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| CARD_AUTHORIZATION_REQUESTED | &quot;card_authorization_requested&quot; |
| DIGITAL_WALLET_TOKEN_REQUESTED | &quot;digital_wallet_token_requested&quot; |
| DIGITAL_WALLET_AUTHENTICATION_REQUESTED | &quot;digital_wallet_authentication_requested&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| RESPONDED | &quot;responded&quot; |
| TIMED_OUT | &quot;timed_out&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REAL_TIME_DECISION | &quot;real_time_decision&quot; |



