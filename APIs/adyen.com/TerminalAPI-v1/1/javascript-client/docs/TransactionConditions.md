# AdyenTerminalApi.TransactionConditions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirerID** | **[Number]** |  | [optional] 
**allowedLoyaltyBrand** | **[String]** |  | [optional] 
**allowedPaymentBrand** | **[String]** |  | [optional] 
**customerLanguage** | **String** | If the language is selected by the Sale System before the request to the POI. | [optional] 
**debitPreferredFlag** | **Boolean** | The preferred type of payment is a debit transaction rather a credit transaction. | [optional] 
**forceEntryMode** | **[String]** |  | [optional] 
**forceOnlineFlag** | **Boolean** | Go online if data sent. | [optional] [default to false]
**loyaltyHandling** | [**LoyaltyHandling**](LoyaltyHandling.md) |  | [optional] 
**merchantCategoryCode** | **String** | The payment implies a specific MCC. | [optional] 



## Enum: [ForceEntryModeEnum]


* `CheckReader` (value: `"CheckReader"`)

* `Contactless` (value: `"Contactless"`)

* `File` (value: `"File"`)

* `ICC` (value: `"ICC"`)

* `Keyed` (value: `"Keyed"`)

* `MagStripe` (value: `"MagStripe"`)

* `Manual` (value: `"Manual"`)

* `RFID` (value: `"RFID"`)

* `Scanned` (value: `"Scanned"`)

* `SynchronousICC` (value: `"SynchronousICC"`)

* `Tapped` (value: `"Tapped"`)




