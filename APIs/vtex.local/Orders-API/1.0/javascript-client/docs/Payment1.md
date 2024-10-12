# OrdersApi.Payment1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardHolder** | **String** | Payment card holder. | 
**cardNumber** | **String** | Payment card number. | 
**connectorResponses** | [**ConnectorResponses**](ConnectorResponses.md) |  | 
**cvv2** | **String** | Card Verification Value (CVV2) is a security code used by payment processors to reduce fraudulent credit and debit card transactions. | 
**dueDate** | **String** | Payment due date. | 
**expireMonth** | **String** | Payment card expire month. | 
**expireYear** | **String** | Payment card expire year. | 
**firstDigits** | **String** | Payment card first digits. | 
**giftCardCaption** | **String** | Gift Card caption. | 
**giftCardId** | **String** | Gift Card ID. | 
**giftCardName** | **String** | Gift Card name. | 
**group** | **String** | It represents the payment method. For each method, it can have the following values:    - **Credit card:** &#x60;creditCard&#x60;     - **Debid card:** &#x60;debitCard&#x60;    - **Bank invoice:** &#x60;bankInvoice&#x60;    - **Promissory:** &#x60;promissory&#x60;     - **Gift card:** &#x60;giftCard&#x60;    - **Pix:** &#x60;instantPayment&#x60; | 
**id** | **String** | Payment ID. | 
**installments** | **Number** | Payment Installments quantity. | 
**lastDigits** | **String** | Payment card last digits. | 
**paymentSystem** | **String** | Payment system ID. | 
**paymentSystemName** | **String** | Payment system name. | 
**redemptionCode** | **String** | Code for the customer to use the Gift Card. | 
**referenceValue** | **Number** | Payment reference Value. | 
**tid** | **String** | Payment transaction ID. | 
**url** | **String** | Payment URL. | 
**value** | **Number** | Payment value. | 


