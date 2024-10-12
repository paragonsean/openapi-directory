

# CardAcquisitionTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedLoyaltyBrand** | **List&lt;String&gt;** |  |  [optional] |
|**allowedPaymentBrand** | **List&lt;String&gt;** |  |  [optional] |
|**cashBackFlag** | **Boolean** |  |  [optional] |
|**customerLanguage** | **String** |  |  [optional] |
|**forceCustomerSelectionFlag** | **Boolean** |  |  [optional] |
|**forceEntryMode** | [**List&lt;ForceEntryModeEnum&gt;**](#List&lt;ForceEntryModeEnum&gt;) |  |  [optional] |
|**loyaltyHandling** | **LoyaltyHandling** |  |  [optional] |
|**paymentType** | **PaymentType** |  |  [optional] |
|**totalAmount** | **BigDecimal** |  |  [optional] |



## Enum: List&lt;ForceEntryModeEnum&gt;

| Name | Value |
|---- | -----|
| CHECK_READER | &quot;CheckReader&quot; |
| CONTACTLESS | &quot;Contactless&quot; |
| FILE | &quot;File&quot; |
| ICC | &quot;ICC&quot; |
| KEYED | &quot;Keyed&quot; |
| MAG_STRIPE | &quot;MagStripe&quot; |
| MANUAL | &quot;Manual&quot; |
| RFID | &quot;RFID&quot; |
| SCANNED | &quot;Scanned&quot; |
| SYNCHRONOUS_ICC | &quot;SynchronousICC&quot; |
| TAPPED | &quot;Tapped&quot; |



