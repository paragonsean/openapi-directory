

# PayAtTable


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationMethod** | [**AuthenticationMethodEnum**](#AuthenticationMethodEnum) | Allowed authentication methods: Magswipe, Manual Entry. |  [optional] |
|**enablePayAtTable** | **Boolean** | Enable Pay at table. |  [optional] |
|**paymentInstrument** | [**PaymentInstrumentEnum**](#PaymentInstrumentEnum) | Sets the allowed payment instrument for Pay at table transactions.  Can be: **cash** or **card**. If not set, the terminal presents both options. |  [optional] |



## Enum: AuthenticationMethodEnum

| Name | Value |
|---- | -----|
| MAGSWIPE | &quot;MAGSWIPE&quot; |
| MKE | &quot;MKE&quot; |



## Enum: PaymentInstrumentEnum

| Name | Value |
|---- | -----|
| CASH | &quot;Cash&quot; |
| CARD | &quot;Card&quot; |



