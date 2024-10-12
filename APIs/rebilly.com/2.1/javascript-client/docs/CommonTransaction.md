# RebillyRestApi.CommonTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_3ds** | [**ThreeDSecureResult**](ThreeDSecureResult.md) |  | [optional] 
**amount** | **Number** | The transaction&#39;s amount. | [optional] [readonly] 
**billingAddress** | [**ContactObject**](ContactObject.md) | Billing address. | [optional] 
**billingDescriptor** | **String** | The billing descriptor that appears on the periodic billing statement. Commonly 12 or fewer characters for a credit card statement.  | [optional] [readonly] 
**childTransactions** | **[String]** | The child transaction IDs. | [optional] [readonly] 
**createdTime** | **Date** | Transaction created time. | [optional] [readonly] 
**currency** | **String** | ISO 4217 alphabetic currency code. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | The сustomer&#39;s ID. | [optional] 
**description** | **String** | The payment description. | [optional] 
**gatewayName** | [**GatewayName**](GatewayName.md) | Payment Gateway name, available only after the gateway is selected for the transaction.  | [optional] [readonly] 
**has3ds** | **Boolean** |  | [optional] [readonly] 
**hasAmountAdjustment** | **Boolean** | True if transaction has amount adjustment. | [optional] [readonly] 
**id** | **String** | The transaction ID. | [optional] [readonly] 
**invoiceIds** | **[String]** | The invoice IDs related to transaction. | [optional] [readonly] 
**isRebill** | **Boolean** |  | [optional] [readonly] 
**isRetry** | **Boolean** | True if this transaction is retry. | [optional] [readonly] 
**parentTransactionId** | **String** | The parent&#39;s transaction ID. | [optional] [readonly] 
**paymentInstrument** | [**InstrumentReference**](InstrumentReference.md) |  | [optional] 
**planIds** | **[String]** | The plan IDs related to transaction&#39;s order(s). | [optional] [readonly] 
**processedTime** | **Date** | Transaction processed time. | [optional] [readonly] 
**purchaseAmount** | **Number** | The amount actually purchased which may have differed from the originally requested amount in case of an adjustment. | [optional] [readonly] 
**purchaseCurrency** | **String** | ISO 4217 alphabetic currency code. | [optional] [readonly] 
**rebillNumber** | **Number** | The transaction&#39;s rebill number. | [optional] [readonly] 
**redirectUrl** | **String** | The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website&#39;s configured URL. | [optional] 
**requestAmount** | **Number** | The amount in the payment request. If adjusted, the purchase amount and billing amount may vary from it. | [optional] [readonly] 
**requestCurrency** | **String** | ISO 4217 alphabetic currency code. | [optional] [readonly] 
**requestId** | **String** | The transaction&#39;s request ID.  This ID must be unique within a 24 hour period. Use this field to prevent duplicated transactions. | [optional] 
**result** | **String** | Transaction result. | [optional] [readonly] 
**retryNumber** | **Number** | The position in the sequence of retries. | [optional] [readonly] 
**status** | **String** | Transaction status. | [optional] [readonly] 
**subscriptionIds** | **[String]** | The orders IDs related to transaction&#39;s invoice(s). | [optional] [readonly] 
**type** | **String** | Transaction type. | [optional] [readonly] 
**updatedTime** | **Date** | Transaction updated time. | [optional] [readonly] 
**websiteId** | **String** | The website ID. | [optional] [readonly] 



## Enum: ResultEnum


* `abandoned` (value: `"abandoned"`)

* `approved` (value: `"approved"`)

* `canceled` (value: `"canceled"`)

* `declined` (value: `"declined"`)

* `unknown` (value: `"unknown"`)





## Enum: StatusEnum


* `completed` (value: `"completed"`)

* `conn-error` (value: `"conn-error"`)

* `disputed` (value: `"disputed"`)

* `never-sent` (value: `"never-sent"`)

* `offsite` (value: `"offsite"`)

* `partially-refunded` (value: `"partially-refunded"`)

* `pending` (value: `"pending"`)

* `refunded` (value: `"refunded"`)

* `sending` (value: `"sending"`)

* `suspended` (value: `"suspended"`)

* `timeout` (value: `"timeout"`)

* `voided` (value: `"voided"`)

* `waiting-approval` (value: `"waiting-approval"`)

* `waiting-capture` (value: `"waiting-capture"`)

* `waiting-gateway` (value: `"waiting-gateway"`)

* `waiting-refund` (value: `"waiting-refund"`)





## Enum: TypeEnum


* `3ds-authentication` (value: `"3ds-authentication"`)

* `authorize` (value: `"authorize"`)

* `capture` (value: `"capture"`)

* `credit` (value: `"credit"`)

* `refund` (value: `"refund"`)

* `sale` (value: `"sale"`)

* `void` (value: `"void"`)




