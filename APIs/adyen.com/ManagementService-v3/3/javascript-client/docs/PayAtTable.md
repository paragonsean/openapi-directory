# ManagementApi.PayAtTable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationMethod** | **String** | Allowed authentication methods: Magswipe, Manual Entry. | [optional] 
**enablePayAtTable** | **Boolean** | Enable Pay at table. | [optional] 
**paymentInstrument** | **String** | Sets the allowed payment instrument for Pay at table transactions.  Can be: **cash** or **card**. If not set, the terminal presents both options. | [optional] 



## Enum: AuthenticationMethodEnum


* `MAGSWIPE` (value: `"MAGSWIPE"`)

* `MKE` (value: `"MKE"`)





## Enum: PaymentInstrumentEnum


* `Cash` (value: `"Cash"`)

* `Card` (value: `"Card"`)




