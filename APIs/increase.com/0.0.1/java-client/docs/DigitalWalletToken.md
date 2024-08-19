

# DigitalWalletToken

Fields related to a digital wallet token provisioning attempt.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardId** | **String** | The identifier of the Card that is being tokenized. |  |
|**cardProfileId** | **String** | The identifier of the Card Profile that was set via the real time decision. This will be null until the real time decision is responded to or if the real time decision did not set a card profile. |  |
|**decision** | [**DecisionEnum**](#DecisionEnum) | Whether or not the provisioning request was approved. This will be null until the real time decision is responded to. |  |
|**digitalWallet** | [**DigitalWalletEnum**](#DigitalWalletEnum) | The digital wallet app being used. |  |



## Enum: DecisionEnum

| Name | Value |
|---- | -----|
| APPROVE | &quot;approve&quot; |
| DECLINE | &quot;decline&quot; |



## Enum: DigitalWalletEnum

| Name | Value |
|---- | -----|
| APPLE_PAY | &quot;apple_pay&quot; |
| GOOGLE_PAY | &quot;google_pay&quot; |



