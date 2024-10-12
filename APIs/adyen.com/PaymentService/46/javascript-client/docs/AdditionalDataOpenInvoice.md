# AdyenPaymentApi.AdditionalDataOpenInvoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openinvoicedataMerchantData** | **String** | Holds different merchant data points like product, purchase, customer, and so on. It takes data in a Base64 encoded string.  The &#x60;merchantData&#x60; parameter needs to be added to the &#x60;openinvoicedata&#x60; signature at the end.  Since the field is optional, if it&#39;s not included it does not impact computing the merchant signature.  Applies only to Klarna.  You can contact Klarna for the format and structure of the string. | [optional] 
**openinvoicedataNumberOfLines** | **String** | The number of invoice lines included in &#x60;openinvoicedata&#x60;.  There needs to be at least one line, so &#x60;numberOfLines&#x60; needs to be at least 1. | [optional] 
**openinvoicedataRecipientFirstName** | **String** | First name of the recipient. If the delivery address and the billing address are different, specify the &#x60;recipientFirstName&#x60; and &#x60;recipientLastName&#x60; to share the delivery address with Klarna. Otherwise, only the billing address is shared with Klarna. | [optional] 
**openinvoicedataRecipientLastName** | **String** | Last name of the recipient. If the delivery address and the billing address are different, specify the &#x60;recipientFirstName&#x60; and &#x60;recipientLastName&#x60; to share the delivery address with Klarna. Otherwise, only the billing address is shared with Klarna. | [optional] 
**openinvoicedataLineItemNrCurrencyCode** | **String** | The three-character ISO currency code. | [optional] 
**openinvoicedataLineItemNrDescription** | **String** | A text description of the product the invoice line refers to. | [optional] 
**openinvoicedataLineItemNrItemAmount** | **String** | The price for one item in the invoice line, represented in minor units.  The due amount for the item, VAT excluded. | [optional] 
**openinvoicedataLineItemNrItemId** | **String** | A unique id for this item. Required for RatePay if the description of each item is not unique. | [optional] 
**openinvoicedataLineItemNrItemVatAmount** | **String** | The VAT due for one item in the invoice line, represented in minor units. | [optional] 
**openinvoicedataLineItemNrItemVatPercentage** | **String** | The VAT percentage for one item in the invoice line, represented in minor units.  For example, 19% VAT is specified as 1900. | [optional] 
**openinvoicedataLineItemNrNumberOfItems** | **String** | The number of units purchased of a specific product. | [optional] 
**openinvoicedataLineItemNrReturnShippingCompany** | **String** | Name of the shipping company handling the the return shipment. | [optional] 
**openinvoicedataLineItemNrReturnTrackingNumber** | **String** | The tracking number for the return of the shipment. | [optional] 
**openinvoicedataLineItemNrReturnTrackingUri** | **String** | URI where the customer can track the return of their shipment. | [optional] 
**openinvoicedataLineItemNrShippingCompany** | **String** | Name of the shipping company handling the delivery. | [optional] 
**openinvoicedataLineItemNrShippingMethod** | **String** | Shipping method. | [optional] 
**openinvoicedataLineItemNrTrackingNumber** | **String** | The tracking number for the shipment. | [optional] 
**openinvoicedataLineItemNrTrackingUri** | **String** | URI where the customer can track their shipment. | [optional] 


