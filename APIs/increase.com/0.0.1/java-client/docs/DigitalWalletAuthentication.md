

# DigitalWalletAuthentication

Fields related to a digital wallet authentication attempt.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardId** | **String** | The identifier of the Card that is being tokenized. |  |
|**channel** | [**ChannelEnum**](#ChannelEnum) | The channel to send the card user their one-time passcode. |  |
|**digitalWallet** | [**DigitalWalletEnum**](#DigitalWalletEnum) | The digital wallet app being used. |  |
|**email** | **String** | The email to send the one-time passcode to if &#x60;channel&#x60; is equal to &#x60;email&#x60;. |  |
|**oneTimePasscode** | **String** | The one-time passcode to send the card user. |  |
|**phone** | **String** | The phone number to send the one-time passcode to if &#x60;channel&#x60; is equal to &#x60;sms&#x60;. |  |
|**result** | [**ResultEnum**](#ResultEnum) | Whether your application successfully delivered the one-time passcode. |  |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |
| EMAIL | &quot;email&quot; |



## Enum: DigitalWalletEnum

| Name | Value |
|---- | -----|
| APPLE_PAY | &quot;apple_pay&quot; |
| GOOGLE_PAY | &quot;google_pay&quot; |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |



