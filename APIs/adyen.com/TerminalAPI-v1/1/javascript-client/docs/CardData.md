# AdyenTerminalApi.CardData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedProduct** | [**[AllowedProduct]**](AllowedProduct.md) |  | [optional] 
**allowedProductCode** | **[Number]** |  | [optional] 
**cardCountryCode** | **Number** | If available in the card. | [optional] 
**customerOrder** | [**[CustomerOrder]**](CustomerOrder.md) |  | [optional] 
**entryMode** | **[String]** |  | [optional] 
**maskedPan** | **String** |  | [optional] 
**paymentAccountRef** | **String** |  | [optional] 
**paymentBrand** | **String** | If card PAN is readable . | [optional] 
**paymentToken** | [**PaymentToken**](PaymentToken.md) |  | [optional] 
**protectedCardData** | **String** | SensitiveCardData protected by CMS EnvelopedData. | [optional] 
**sensitiveCardData** | [**SensitiveCardData**](SensitiveCardData.md) |  | [optional] 



## Enum: [EntryModeEnum]


* `Contactless` (value: `"Contactless"`)

* `File` (value: `"File"`)

* `ICC` (value: `"ICC"`)

* `Keyed` (value: `"Keyed"`)

* `MagStripe` (value: `"MagStripe"`)

* `Manual` (value: `"Manual"`)

* `Mobile` (value: `"Mobile"`)

* `RFID` (value: `"RFID"`)

* `Scanned` (value: `"Scanned"`)

* `SynchronousICC` (value: `"SynchronousICC"`)

* `Tapped` (value: `"Tapped"`)




