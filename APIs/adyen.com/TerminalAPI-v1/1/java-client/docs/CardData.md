

# CardData

Allows acquisition of the card data by the Sale System before the Payment, CardAcquisition  or BalanceInquiry request to the POI. It could also be sent in the CardAcquisition response, to be processed by the Sale System. Information related to the payment card used for the transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedProduct** | [**List&lt;AllowedProduct&gt;**](AllowedProduct.md) |  |  [optional] |
|**allowedProductCode** | **List&lt;Integer&gt;** |  |  [optional] |
|**cardCountryCode** | **Integer** | If available in the card. |  [optional] |
|**customerOrder** | [**List&lt;CustomerOrder&gt;**](CustomerOrder.md) |  |  [optional] |
|**entryMode** | [**List&lt;EntryModeEnum&gt;**](#List&lt;EntryModeEnum&gt;) |  |  [optional] |
|**maskedPan** | **String** |  |  [optional] |
|**paymentAccountRef** | **String** |  |  [optional] |
|**paymentBrand** | **String** | If card PAN is readable . |  [optional] |
|**paymentToken** | [**PaymentToken**](PaymentToken.md) |  |  [optional] |
|**protectedCardData** | **String** | SensitiveCardData protected by CMS EnvelopedData. |  [optional] |
|**sensitiveCardData** | [**SensitiveCardData**](SensitiveCardData.md) |  |  [optional] |



## Enum: List&lt;EntryModeEnum&gt;

| Name | Value |
|---- | -----|
| CONTACTLESS | &quot;Contactless&quot; |
| FILE | &quot;File&quot; |
| ICC | &quot;ICC&quot; |
| KEYED | &quot;Keyed&quot; |
| MAG_STRIPE | &quot;MagStripe&quot; |
| MANUAL | &quot;Manual&quot; |
| MOBILE | &quot;Mobile&quot; |
| RFID | &quot;RFID&quot; |
| SCANNED | &quot;Scanned&quot; |
| SYNCHRONOUS_ICC | &quot;SynchronousICC&quot; |
| TAPPED | &quot;Tapped&quot; |



