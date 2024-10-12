

# CommonTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_3ds** | [**ThreeDSecureResult**](ThreeDSecureResult.md) |  |  [optional] |
|**amount** | **Double** | The transaction&#39;s amount. |  [optional] [readonly] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | Billing address. |  [optional] |
|**billingDescriptor** | **String** | The billing descriptor that appears on the periodic billing statement. Commonly 12 or fewer characters for a credit card statement.  |  [optional] [readonly] |
|**childTransactions** | **List&lt;String&gt;** | The child transaction IDs. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Transaction created time. |  [optional] [readonly] |
|**currency** | **String** | ISO 4217 alphabetic currency code. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | The сustomer&#39;s ID. |  [optional] |
|**description** | **String** | The payment description. |  [optional] |
|**gatewayName** | **GatewayName** | Payment Gateway name, available only after the gateway is selected for the transaction.  |  [optional] [readonly] |
|**has3ds** | **Boolean** |  |  [optional] [readonly] |
|**hasAmountAdjustment** | **Boolean** | True if transaction has amount adjustment. |  [optional] [readonly] |
|**id** | **String** | The transaction ID. |  [optional] [readonly] |
|**invoiceIds** | **List&lt;String&gt;** | The invoice IDs related to transaction. |  [optional] [readonly] |
|**isRebill** | **Boolean** |  |  [optional] [readonly] |
|**isRetry** | **Boolean** | True if this transaction is retry. |  [optional] [readonly] |
|**parentTransactionId** | **String** | The parent&#39;s transaction ID. |  [optional] [readonly] |
|**paymentInstrument** | [**InstrumentReference**](InstrumentReference.md) |  |  [optional] |
|**planIds** | **List&lt;String&gt;** | The plan IDs related to transaction&#39;s order(s). |  [optional] [readonly] |
|**processedTime** | **OffsetDateTime** | Transaction processed time. |  [optional] [readonly] |
|**purchaseAmount** | **Double** | The amount actually purchased which may have differed from the originally requested amount in case of an adjustment. |  [optional] [readonly] |
|**purchaseCurrency** | **String** | ISO 4217 alphabetic currency code. |  [optional] [readonly] |
|**rebillNumber** | **Integer** | The transaction&#39;s rebill number. |  [optional] [readonly] |
|**redirectUrl** | **URI** | The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website&#39;s configured URL. |  [optional] |
|**requestAmount** | **Double** | The amount in the payment request. If adjusted, the purchase amount and billing amount may vary from it. |  [optional] [readonly] |
|**requestCurrency** | **String** | ISO 4217 alphabetic currency code. |  [optional] [readonly] |
|**requestId** | **String** | The transaction&#39;s request ID.  This ID must be unique within a 24 hour period. Use this field to prevent duplicated transactions. |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | Transaction result. |  [optional] [readonly] |
|**retryNumber** | **Integer** | The position in the sequence of retries. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Transaction status. |  [optional] [readonly] |
|**subscriptionIds** | **List&lt;String&gt;** | The orders IDs related to transaction&#39;s invoice(s). |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Transaction type. |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | Transaction updated time. |  [optional] [readonly] |
|**websiteId** | **String** | The website ID. |  [optional] [readonly] |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| ABANDONED | &quot;abandoned&quot; |
| APPROVED | &quot;approved&quot; |
| CANCELED | &quot;canceled&quot; |
| DECLINED | &quot;declined&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;completed&quot; |
| CONN_ERROR | &quot;conn-error&quot; |
| DISPUTED | &quot;disputed&quot; |
| NEVER_SENT | &quot;never-sent&quot; |
| OFFSITE | &quot;offsite&quot; |
| PARTIALLY_REFUNDED | &quot;partially-refunded&quot; |
| PENDING | &quot;pending&quot; |
| REFUNDED | &quot;refunded&quot; |
| SENDING | &quot;sending&quot; |
| SUSPENDED | &quot;suspended&quot; |
| TIMEOUT | &quot;timeout&quot; |
| VOIDED | &quot;voided&quot; |
| WAITING_APPROVAL | &quot;waiting-approval&quot; |
| WAITING_CAPTURE | &quot;waiting-capture&quot; |
| WAITING_GATEWAY | &quot;waiting-gateway&quot; |
| WAITING_REFUND | &quot;waiting-refund&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| _3DS_AUTHENTICATION | &quot;3ds-authentication&quot; |
| AUTHORIZE | &quot;authorize&quot; |
| CAPTURE | &quot;capture&quot; |
| CREDIT | &quot;credit&quot; |
| REFUND | &quot;refund&quot; |
| SALE | &quot;sale&quot; |
| VOID | &quot;void&quot; |



