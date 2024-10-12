

# Quote


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandingThemeID** | **UUID** | See BrandingThemes |  [optional] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**currencyCode** | **CurrencyCode** |  |  [optional] |
|**currencyRate** | **Double** | The currency rate for a multicurrency quote |  [optional] |
|**date** | **String** | Date quote was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation |  [optional] |
|**dateString** | **String** | Date the quote was issued (YYYY-MM-DD) |  [optional] |
|**expiryDate** | **String** | Date the quote expires – YYYY-MM-DD. |  [optional] |
|**expiryDateString** | **String** | Date the quote expires – YYYY-MM-DD. |  [optional] |
|**lineAmountTypes** | **QuoteLineAmountTypes** |  |  [optional] |
|**lineItems** | [**List&lt;LineItem&gt;**](LineItem.md) | See LineItems |  [optional] |
|**quoteID** | **UUID** | QuoteID GUID is automatically generated and is returned after create or GET. |  [optional] |
|**quoteNumber** | **String** | Unique alpha numeric code identifying a quote (Max Length &#x3D; 255) |  [optional] |
|**reference** | **String** | Additional reference number |  [optional] |
|**status** | **QuoteStatusCodes** |  |  [optional] |
|**statusAttributeString** | **String** | A string to indicate if a invoice status |  [optional] |
|**subTotal** | **Double** | Total of quote excluding taxes. |  [optional] [readonly] |
|**summary** | **String** | Summary text for the quote |  [optional] |
|**terms** | **String** | Terms of the quote |  [optional] |
|**title** | **String** | Title text for the quote |  [optional] |
|**total** | **Double** | Total of Quote tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts |  [optional] [readonly] |
|**totalDiscount** | **Double** | Total of discounts applied on the quote line items |  [optional] [readonly] |
|**totalTax** | **Double** | Total tax on quote |  [optional] [readonly] |
|**updatedDateUTC** | **String** | Last modified date UTC format |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



