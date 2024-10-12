

# InvoicePaymentRequest

Represents a payment request for an [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice). Invoices can specify a maximum of 13 payment requests, with up to 12 `INSTALLMENT` request types. For more information,  see [Payment requests](https://developer.squareup.com/docs/invoices-api/overview#payment-requests).  Adding `INSTALLMENT` payment requests to an invoice requires an  [Invoices Plus subscription](https://developer.squareup.com/docs/invoices-api/overview#invoices-plus-subscription).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automaticPaymentSource** | **String** | The payment method for an automatic payment.  The default value is &#x60;NONE&#x60;. |  [optional] |
|**cardId** | **String** | The ID of the credit or debit card on file to charge for the payment request. To get the cards on file for a customer, call [ListCards](https://developer.squareup.com/reference/square_2021-08-18/cards-api/list-cards) and include the &#x60;customer_id&#x60; of the invoice recipient. |  [optional] |
|**computedAmountMoney** | [**Money**](Money.md) |  |  [optional] |
|**dueDate** | **String** | The due date (in the invoice&#39;s time zone) for the payment request, in &#x60;YYYY-MM-DD&#x60; format. This field is required to create a payment request.  After this date, the invoice becomes overdue. For example, a payment &#x60;due_date&#x60; of 2021-03-09 with a &#x60;timezone&#x60; of America/Los\\_Angeles becomes overdue at midnight on March 9 in America/Los\\_Angeles (which equals a UTC timestamp of 2021-03-10T08:00:00Z). |  [optional] |
|**fixedAmountRequestedMoney** | [**Money**](Money.md) |  |  [optional] |
|**percentageRequested** | **String** | Specifies the amount for the payment request in percentage:  - When the payment &#x60;request_type&#x60; is &#x60;DEPOSIT&#x60;, it is the percentage of the order&#39;s total amount. - When the payment &#x60;request_type&#x60; is &#x60;INSTALLMENT&#x60;, it is the percentage of the order&#39;s total less  the deposit, if requested. The sum of the &#x60;percentage_requested&#x60; in all installment  payment requests must be equal to 100.  You cannot specify this when the payment &#x60;request_type&#x60; is &#x60;BALANCE&#x60; or when the  payment request specifies the &#x60;fixed_amount_requested_money&#x60; field. |  [optional] |
|**reminders** | [**List&lt;InvoicePaymentReminder&gt;**](InvoicePaymentReminder.md) | A list of one or more reminders to send for the payment request. |  [optional] |
|**requestMethod** | **String** | Indicates how Square processes the payment request. DEPRECATED at version 2021-01-21. Replaced by the &#x60;Invoice.delivery_method&#x60; and &#x60;InvoicePaymentRequest.automatic_payment_source&#x60; fields.  One of the following is required when creating an invoice: - (Recommended) The &#x60;delivery_method&#x60; field of the invoice. To configure an automatic payment, the &#x60;automatic_payment_source&#x60; field of the payment request is also required. - This &#x60;request_method&#x60; field. Note that &#x60;invoice&#x60; objects returned in responses do not include &#x60;request_method&#x60;. |  [optional] |
|**requestType** | **String** | Identifies the payment request type. This type defines how the payment request amount is determined.  This field is required to create a payment request. |  [optional] |
|**roundingAdjustmentIncludedMoney** | [**Money**](Money.md) |  |  [optional] |
|**tippingEnabled** | **Boolean** | If set to true, the Square-hosted invoice page (the &#x60;public_url&#x60; field of the invoice)  provides a place for the customer to pay a tip.   This field is allowed only on the final payment request   and the payment &#x60;request_type&#x60; must be &#x60;BALANCE&#x60; or &#x60;INSTALLMENT&#x60;. |  [optional] |
|**totalCompletedAmountMoney** | [**Money**](Money.md) |  |  [optional] |
|**uid** | **String** | The Square-generated ID of the payment request in an [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice). |  [optional] |



