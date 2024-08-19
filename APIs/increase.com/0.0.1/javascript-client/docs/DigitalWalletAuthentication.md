# IncreaseApi.DigitalWalletAuthentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardId** | **String** | The identifier of the Card that is being tokenized. | 
**channel** | **String** | The channel to send the card user their one-time passcode. | 
**digitalWallet** | **String** | The digital wallet app being used. | 
**email** | **String** | The email to send the one-time passcode to if &#x60;channel&#x60; is equal to &#x60;email&#x60;. | 
**oneTimePasscode** | **String** | The one-time passcode to send the card user. | 
**phone** | **String** | The phone number to send the one-time passcode to if &#x60;channel&#x60; is equal to &#x60;sms&#x60;. | 
**result** | **String** | Whether your application successfully delivered the one-time passcode. | 



## Enum: ChannelEnum


* `sms` (value: `"sms"`)

* `email` (value: `"email"`)





## Enum: DigitalWalletEnum


* `apple_pay` (value: `"apple_pay"`)

* `google_pay` (value: `"google_pay"`)





## Enum: ResultEnum


* `success` (value: `"success"`)

* `failure` (value: `"failure"`)




