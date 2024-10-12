

# Payment

Payment details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Payment&#39;s account ID. |  |
|**bankIssuedInvoiceBarCodeNumber** | **String** | Number of the bank issued invoice bar code. |  |
|**bankIssuedInvoiceBarCodeType** | **String** | Type of the bank issued invoice bar code. |  |
|**bankIssuedInvoiceIdentificationNumber** | **String** | Numeric sequence that identifies the bank issued invoice. |  |
|**bankIssuedInvoiceIdentificationNumberFormatted** | **String** | Bank issued invoice ID formatted. |  |
|**billingAddress** | **Object** | Billing address information. |  |
|**cardHolder** | **String** | Name of the person who owns the card. |  |
|**cardNumber** | **String** | Numeric sequence of the card used in the transaction. |  |
|**connectorResponses** | [**PaymentConnectorResponses**](PaymentConnectorResponses.md) |  |  |
|**cvv2** | **String** | Card Verification Value (CVV2) is a security code used by payment processors to reduce fraudulent credit and debit card transactions. |  |
|**dueDate** | **String** | Payment due date, with the format &#x60;yyyy-mm-dd&#x60;. |  |
|**expireMonth** | **String** | Expire month of the card used in the transaction (2-digits). |  |
|**expireYear** | **String** | Expire year of the card used in the transaction (4-digits). |  |
|**firstDigits** | **String** | Fist digits of the card used in the transaction. |  |
|**giftCardAsDiscount** | **Boolean** | When this field is set as &#x60;true&#x60;, the Gift Card is a discount over the price, and when set as &#x60;false&#x60;, it is not a discount. |  |
|**giftCardCaption** | **String** | Gift Card&#39;s caption. |  |
|**giftCardId** | **String** | Gift Card&#39;s ID. |  |
|**giftCardName** | **String** | Gift Card&#39;s name. |  |
|**giftCardProvider** | **String** | Gift Card provider&#39;s ID. |  |
|**group** | **String** | Name of the collection the Gift Card belongs to. |  |
|**id** | **String** | VTEX payment ID that can be used as unique identifier. |  |
|**installments** | **Integer** | Number of payment installments. |  |
|**koinUrl** | **String** | Payment&#39;s account ID. |  |
|**lastDigits** | **String** | Last digits of the card used in the transaction. |  |
|**parentAccountId** | **String** | This field retrieves the main account if the payment was made in a subaccount. |  |
|**paymentSystem** | **String** | Payment system&#39;s ID. |  |
|**paymentSystemName** | **String** | Payment system&#39;s name. |  |
|**redemptionCode** | **String** | Code for the customer to use the Gift Card. |  |
|**referenceValue** | **Integer** | Payment&#39;s reference value in cents. |  |
|**tid** | **String** | Provider&#39;s unique identifier for the transaction. |  |
|**url** | **String** | Payment&#39;s URL. |  |
|**value** | **Integer** | Payment&#39;s final amount in cents. |  |



