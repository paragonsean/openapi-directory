

# StoredValueAccountID

It contains the identifications of the stored value account or the stored value card, and the associated product sold by the Sale System for stored value requests. Identification of the stored value account or the stored value card.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entryMode** | [**List&lt;EntryModeEnum&gt;**](#List&lt;EntryModeEnum&gt;) |  |  |
|**expiryDate** | **Integer** |  |  [optional] |
|**identificationType** | **IdentificationType** |  |  |
|**ownerName** | **String** |  |  [optional] |
|**storedValueAccountType** | **StoredValueAccountType** |  |  |
|**storedValueID** | **String** |  |  |
|**storedValueProvider** | **String** |  |  [optional] |



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



