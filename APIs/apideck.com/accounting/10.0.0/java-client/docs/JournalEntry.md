

# JournalEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**currencyRate** | **BigDecimal** | Currency Exchange Rate at the time entity was recorded/generated. |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**journalSymbol** | **String** | Journal symbol of the entry. For example IND for indirect costs |  [optional] |
|**lineItems** | [**List&lt;JournalEntryLineItem&gt;**](JournalEntryLineItem.md) | Requires a minimum of 2 line items that sum to 0 |  [optional] |
|**memo** | **String** | Reference for the journal entry. |  [optional] |
|**number** | **String** | Journal entry number. |  [optional] |
|**postedAt** | **OffsetDateTime** | This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated. |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**taxCode** | **String** | Applicable tax id/code override if tax is not supplied on a line item basis. |  [optional] |
|**taxType** | **String** | The specific category of tax associated with a transaction like sales or purchase |  [optional] |
|**title** | **String** | Journal entry title |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



