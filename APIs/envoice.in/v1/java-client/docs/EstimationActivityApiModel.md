

# EstimationActivityApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**estimationNumber** | **String** | Indicates to which estimation this activity refers to |  [optional] |
|**id** | **Integer** | Id of estimation activity |  [optional] |
|**link** | **String** | Url which point out to a certain activity action. Ex: Click to view the payment |  [optional] |
|**message** | **String** | Message associated with the activity |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the activity |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;Created&quot; |
| DRAFT | &quot;Draft&quot; |
| CLONED | &quot;Cloned&quot; |
| SENT_VIA_EMAIL | &quot;SentViaEmail&quot; |
| SENT_VIA_SMS | &quot;SentViaSms&quot; |
| SENT_REMINDER_VIA_EMAIL | &quot;SentReminderViaEmail&quot; |
| SENT_REMINDER_VIA_SMS | &quot;SentReminderViaSms&quot; |
| OPENED | &quot;Opened&quot; |
| VIEWED | &quot;Viewed&quot; |
| REJECTED | &quot;Rejected&quot; |
| UPDATED | &quot;Updated&quot; |
| PAID | &quot;Paid&quot; |
| UNPAID | &quot;Unpaid&quot; |
| OVERDUE | &quot;Overdue&quot; |
| NEW_MANUAL_PAYMENT | &quot;NewManualPayment&quot; |
| NEW_PAYMENT_WITH_PAYPAL | &quot;NewPaymentWithPaypal&quot; |
| NEW_PAYMENT_WITH_STRIPE | &quot;NewPaymentWithStripe&quot; |
| NEW_PAYMENT_WITH_PAYONEER | &quot;NewPaymentWithPayoneer&quot; |
| SENT_TO_ACCOUNTANT | &quot;SentToAccountant&quot; |
| DOWNLOADED_AS_PDF | &quot;DownloadedAsPdf&quot; |
| MARK_AS_PAID_BY_THE_CLIENT | &quot;MarkAsPaidByTheClient&quot; |
| OPENED_ATTACHMENT | &quot;OpenedAttachment&quot; |
| NEW_PAYMENT_WITH_SQUARE | &quot;NewPaymentWithSquare&quot; |
| NEW_PAYMENT_WITH_KLIK_AND_PAY | &quot;NewPaymentWithKlikAndPay&quot; |
| NEW_PAYMENT_WITH_RAZORPAY | &quot;NewPaymentWithRazorpay&quot; |
| NEW_PAYMENT_WITH_WEPAY | &quot;NewPaymentWithWepay&quot; |
| NEW_PAYMENT_WITH_HALKBANK | &quot;NewPaymentWithHalkbank&quot; |
| CHANGE_STATUS | &quot;ChangeStatus&quot; |
| ORDER_UPDATED | &quot;OrderUpdated&quot; |
| ORDER_CREATED | &quot;OrderCreated&quot; |
| NEW_PAYMENT_WITH_TWO_CHECKOUT | &quot;NewPaymentWithTwoCheckout&quot; |
| NEW_PAYMENT_WITH_PAYMENT_WALL | &quot;NewPaymentWithPaymentWall&quot; |
| NEW_PAYMENT_WITH_BAMBORA_EU | &quot;NewPaymentWithBamboraEU&quot; |
| NEW_PAYMENT_WITH_BAMBORA_NA | &quot;NewPaymentWithBamboraNA&quot; |
| VOID | &quot;Void&quot; |
| NEW_PAYMENT_WITH_NLB | &quot;NewPaymentWithNlb&quot; |
| NEW_PAYMENT_WITH_AUTHORIZE_NET | &quot;NewPaymentWithAuthorizeNet&quot; |
| NEW_PAYMENT_WITH_BRAINTREE | &quot;NewPaymentWithBraintree&quot; |
| ESTIMATION_CREATED | &quot;EstimationCreated&quot; |
| ESTIMATION_DRAFT | &quot;EstimationDraft&quot; |
| ESTIMATION_CLONED | &quot;EstimationCloned&quot; |
| ESTIMATION_SENT_VIA_EMAIL | &quot;EstimationSentViaEmail&quot; |
| ESTIMATION_OPENED | &quot;EstimationOpened&quot; |
| ESTIMATION_VIEWED | &quot;EstimationViewed&quot; |
| ESTIMATION_ACCEPTED | &quot;EstimationAccepted&quot; |
| ESTIMATION_REJECTED | &quot;EstimationRejected&quot; |
| ESTIMATION_UPDATED | &quot;EstimationUpdated&quot; |
| ESTIMATION_DOWNLOADED_AS_PDF | &quot;EstimationDownloadedAsPdf&quot; |
| INVOICE_DIGITALLY_SIGNED | &quot;InvoiceDigitallySigned&quot; |



