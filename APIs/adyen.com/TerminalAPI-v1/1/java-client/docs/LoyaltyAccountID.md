

# LoyaltyAccountID

In the Payment or the Loyalty Request message, it allows to identify the loyalty account by the Sale Terminal instead of the POI Terminal (e.g. because the account identification is a bar-code read by the Cashier on a scanner device). Identification of a Loyalty account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entryMode** | [**List&lt;EntryModeEnum&gt;**](#List&lt;EntryModeEnum&gt;) |  |  |
|**identificationSupport** | **IdentificationSupport** |  |  [optional] |
|**identificationType** | **IdentificationType** |  |  |
|**loyaltyID** | **String** |  |  |



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



