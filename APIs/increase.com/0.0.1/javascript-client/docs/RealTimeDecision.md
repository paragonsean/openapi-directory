# IncreaseApi.RealTimeDecision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardAuthorization** | [**CardAuthorization1**](CardAuthorization1.md) |  | 
**category** | **String** | The category of the Real-Time Decision. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Real-Time Decision was created. | 
**digitalWalletAuthentication** | [**DigitalWalletAuthentication**](DigitalWalletAuthentication.md) |  | 
**digitalWalletToken** | [**DigitalWalletToken**](DigitalWalletToken.md) |  | 
**id** | **String** | The Real-Time Decision identifier. | 
**status** | **String** | The status of the Real-Time Decision. | 
**timeoutAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which your application can no longer respond to the Real-Time Decision. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;real_time_decision&#x60;. | 



## Enum: CategoryEnum


* `card_authorization_requested` (value: `"card_authorization_requested"`)

* `digital_wallet_token_requested` (value: `"digital_wallet_token_requested"`)

* `digital_wallet_authentication_requested` (value: `"digital_wallet_authentication_requested"`)





## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `responded` (value: `"responded"`)

* `timed_out` (value: `"timed_out"`)





## Enum: TypeEnum


* `real_time_decision` (value: `"real_time_decision"`)




