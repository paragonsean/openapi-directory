

# TransactionConditions

Conditions on which the transaction must be processed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acquirerID** | **List&lt;Integer&gt;** |  |  [optional] |
|**allowedLoyaltyBrand** | **List&lt;String&gt;** |  |  [optional] |
|**allowedPaymentBrand** | **List&lt;String&gt;** |  |  [optional] |
|**customerLanguage** | **String** | If the language is selected by the Sale System before the request to the POI. |  [optional] |
|**debitPreferredFlag** | **Boolean** | The preferred type of payment is a debit transaction rather a credit transaction. |  [optional] |
|**forceEntryMode** | [**List&lt;ForceEntryModeEnum&gt;**](#List&lt;ForceEntryModeEnum&gt;) |  |  [optional] |
|**forceOnlineFlag** | **Boolean** | Go online if data sent. |  [optional] |
|**loyaltyHandling** | **LoyaltyHandling** |  |  [optional] |
|**merchantCategoryCode** | **String** | The payment implies a specific MCC. |  [optional] |



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



