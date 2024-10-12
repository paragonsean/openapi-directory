# IncreaseApi.DigitalWalletToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardId** | **String** | The identifier of the Card that is being tokenized. | 
**cardProfileId** | **String** | The identifier of the Card Profile that was set via the real time decision. This will be null until the real time decision is responded to or if the real time decision did not set a card profile. | 
**decision** | **String** | Whether or not the provisioning request was approved. This will be null until the real time decision is responded to. | 
**digitalWallet** | **String** | The digital wallet app being used. | 



## Enum: DecisionEnum


* `approve` (value: `"approve"`)

* `decline` (value: `"decline"`)





## Enum: DigitalWalletEnum


* `apple_pay` (value: `"apple_pay"`)

* `google_pay` (value: `"google_pay"`)




