

# Invoice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIDFK** | **Integer** |  |  [optional] |
|**balance** | **Double** |  |  [optional] |
|**companyIDFK** | **Integer** |  |  [optional] |
|**companyName** | **String** |  |  [optional] |
|**currencyCode** | **String** |  |  [optional] |
|**customerPONumber** | **String** |  |  [optional] |
|**dateCreated** | **OffsetDateTime** |  |  [optional] |
|**dateIssued** | **OffsetDateTime** |  |  [optional] |
|**dateSent** | **OffsetDateTime** |  |  [optional] |
|**dateUpdated** | **OffsetDateTime** |  |  [optional] |
|**dueDate** | **OffsetDateTime** |  |  [optional] |
|**exchangeRate** | **Double** |  |  [optional] |
|**invoiceNumber** | **String** |  |  [optional] |
|**issuer** | [**IssuerDetails**](IssuerDetails.md) |  |  [optional] |
|**lineItems** | [**List&lt;InvoiceLineItem&gt;**](InvoiceLineItem.md) |  |  [optional] |
|**links** | [**InvoiceLinks**](InvoiceLinks.md) |  |  [optional] |
|**notes** | **String** |  |  [optional] |
|**recipient** | [**RecipientDetails**](RecipientDetails.md) |  |  [optional] |
|**subject** | **String** |  |  [optional] |
|**taxAmount** | **Double** |  |  [optional] |
|**totalAmount** | **Double** |  |  [optional] |
|**transactionID** | **Long** |  |  [optional] |
|**transactionPrefix** | **String** |  |  [optional] |
|**transactionStatusCode** | **String** |  |  [optional] |
|**transactionTaxConfigCode** | **String** |  |  [optional] |



