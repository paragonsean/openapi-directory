# RebillyRestApi.PayoutRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The transaction amount. | 
**billingAddress** | [**ContactObject**](ContactObject.md) | Billing address. If not supplied, we use the billing address associated with the payment instrument, and then customer. | [optional] 
**currency** | **String** | ISO 4217 alphabetic currency code. | 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | The customer identifier string. | 
**description** | **String** | The payment description. | [optional] 
**gatewayAccountId** | **String** | Rebilly will select the appropriate payment gateway account for the transaction based on the properties of the transaction and the &#x60;gateway-account-requested&#x60; event rules configurations. If you wish to prevent Rebilly from making the gateway account selection, you may supply a gateway account id here, and it will be used instead. Only use this field if you intend to override the settings. | [optional] 
**invoiceIds** | **[String]** | The array of invoice identifiers. | [optional] 
**isMerchantInitiated** | **Boolean** | True if the transaction was initiated by the merchant. | [optional] [default to false]
**isProcessedOutside** | **Boolean** | True if transaction was processed outside Rebilly. | [optional] [default to false]
**notificationUrl** | **String** | The URL where a server-to-server notification request type &#x60;POST&#x60; with a transaction payload will be sent when the transaction&#39;s result is finalized. Do not trust the notification; follow with a &#x60;GET&#x60; request to confirm the result of the transaction. Please respond with a &#x60;2xx&#x60; HTTP status code, or we will reattempt the request again. You may use &#x60;{id}&#x60; or &#x60;{result}&#x60; as placeholders in the URL and we will replace them with the transaction&#39;s id and result accordingly.  | [optional] 
**paymentInstruction** | [**PaymentInstruction**](PaymentInstruction.md) | Payment instruction. If not supplied, customer&#39;s default payment instrument will be used. | [optional] 
**paymentInstrument** | [**PaymentInstrument**](PaymentInstrument.md) |  | [optional] 
**processedTime** | **Date** | The time the transaction was processed. Can be specified only if transaction was processed outside Rebilly. | [optional] 
**redirectUrl** | **String** | The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website&#39;s configured URL. You may use &#x60;{id}&#x60; or &#x60;{result}&#x60; as placeholders in the URL and we will replace them with the transaction&#39;s id and result accordingly. | [optional] 
**requestId** | **String** | The request id is **recommended**. It prevents duplicate transaction requests within a short period of time. If a duplicate request is sent with the same &#x60;requestId&#x60; it will be ignored to prevent double-billing anyone.  It must be unique within a 24-hour period.  We recommend generating a UUID v4 as its value. | [optional] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  | [optional] 
**websiteId** | **String** | The website identifier string. | 


