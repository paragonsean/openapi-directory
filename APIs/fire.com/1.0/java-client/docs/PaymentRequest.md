

# PaymentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalFields** | **String** | These fields will be dispalyed to the payer when using the hosted option. You can choose to display any of &#x60;ORDER_ID&#x60;, &#x60;PRODUCT_ID&#x60;, &#x60;CUSTOMER_ID&#x60;, &#x60;CUSTOMER_NUMBER&#x60; and &#x60;COMMENT2&#x60; to the payer. |  [optional] |
|**amount** | **Long** | The requested amount to pay. Note the last two digits represent pennies/cents, (e.g., £1.00 &#x3D; 100). |  [optional] |
|**collectFields** | **String** | For the hosted option, the payer will be asked to fill in these fields but they will not be mandatory. You can choose to collect any of the payer&#39;s &#x60;ADDRESS&#x60;, &#x60;REFERENCE&#x60; and/or &#x60;COMMENT1&#x60;. If you choose to collect these fields from the payer, you cannot set &#39;delivery’, &#39;variableReference’ or &#39;comment1’ fields respectively. |  [optional] |
|**currency** | [**Currency**](Currency.md) |  |  [optional] |
|**description** | **String** | A public facing description of the request. This will be shown to the user when they tap or scan the request. |  [optional] |
|**expiry** | **OffsetDateTime** | This is the expiry of the payment request. After this time, the payment cannot be paid. |  [optional] |
|**icanTo** | **Long** | The ican of the account to collect the funds into. Must be one of your fire.com Accounts. |  [optional] |
|**mandatoryFields** | **String** | For the hosted option, these fields will be madatory for the payer to fill in on the hosted payment page. You can choose to collect any the payer&#39;s &#x60;ADDRESS&#x60;, &#x60;REFERENCE&#x60; and/or &#x60;COMMENT1&#x60;. If you choose to collect these fields from the payer, you cannot set &#39;delivery’, &#39;variableReference’ or &#39;comment1’ fields respectively. |  [optional] |
|**maxNumberPayments** | **Integer** | The max number of people who can pay this request. Must be set to 1 for the ECOMMERCE_GOODS and ECOMMERCE_SERVICES types. |  [optional] |
|**myRef** | **String** | An internal description of the request. |  [optional] |
|**orderDetails** | [**OrderDetails**](OrderDetails.md) |  |  [optional] |
|**paymentRequestCode** | **String** | The code that was returned when you created the payment request. |  [optional] |
|**paymentUuid** | **String** | A unique id for the transaction. |  [optional] |
|**returnUrl** | **String** | The merchant return URL where the customer will be re-directed to with the result of the transaction. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the transaction |  [optional] |
|**transactionType** | [**TransactionTypeEnum**](#TransactionTypeEnum) | The type of payment request payment |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of Fire Open Payment that was created |  [optional] |
|**webhookUrl** | **String** | A URL to be called in the background with the details of the payment after the payment is complete |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AWAITING_AUTHORISATION | &quot;AWAITING_AUTHORISATION&quot; |
| AUTHORISED | &quot;AUTHORISED&quot; |
| AWAITING_MULTI_AUTHORISATION | &quot;AWAITING_MULTI_AUTHORISATION&quot; |
| NOT_AUTHORISED | &quot;NOT_AUTHORISED&quot; |
| PAID | &quot;PAID&quot; |
| REJECTED | &quot;REJECTED&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| RECEIVED | &quot;RECEIVED&quot; |



## Enum: TransactionTypeEnum

| Name | Value |
|---- | -----|
| REFUND_REQUEST | &quot;REFUND_REQUEST&quot; |
| PAYMENT | &quot;PAYMENT&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OTHER | &quot;OTHER&quot; |



