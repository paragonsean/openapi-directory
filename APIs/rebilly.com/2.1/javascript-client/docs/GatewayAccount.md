# RebillyRestApi.GatewayAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[GatewayAccountLinksInner]**](GatewayAccountLinksInner.md) | The links related to resource. | [optional] [readonly] 
**acceptedCurrencies** | **[String]** | Accepted currencies (array of the currency three letter codes). | 
**acquirerName** | [**AcquirerName**](AcquirerName.md) |  | [optional] 
**additionalFilters** | **String** | The additional filters are used to determine whether the gateway account can be selected for the transaction to be processed. For example, the filter may put a maximum amount value. If the transaction is above that amount, this gateway account wouldn&#39;t be used. This follows our standard filter format.  | [optional] 
**approvalWindowTtl** | **Number** | The time window (in seconds) allotted for approving an offsite transaction before it is automatically &#x60;abandoned&#x60;. | [optional] [default to 3600]
**cityField** | **String** | The gateway account&#39;s city field (also known as line 2 descriptor). | [optional] 
**createdTime** | **Date** | Gateway Account created time. | [optional] [readonly] 
**dccForceCurrency** | **String** | Force dynamic currency conversion to the specified currency on each sale. Leave it empty to disable force DCC.  | [optional] 
**dccMarkup** | **Number** | Dynamic currency conversion markup in basis points. | [optional] 
**descriptor** | **String** | The gateway account&#39;s descriptor. | [optional] 
**digitalWallets** | [**DigitalWallets**](DigitalWallets.md) |  | [optional] 
**dynamicDescriptor** | **Boolean** | True, if Gateway Account allows dynamic descriptor. | [optional] [default to false]
**excludedDccQuoteCurrencies** | **[String]** | Excluded Dynamic Currency Conversion Quote Currencies. | [optional] 
**gatewayName** | [**GatewayName**](GatewayName.md) |  | 
**id** | **String** | The gateway identifier string. | [optional] [readonly] 
**isDown** | **Boolean** | True if gateway is currently in downtime period. | [optional] [readonly] 
**merchantCategoryCode** | **String** | The gateway account&#39;s merchant category code. | [optional] [default to &#39;0000&#39;]
**method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**monthlyLimit** | **Number** | Monthly Limit. | [optional] 
**organizationId** | **String** | Organization ID. | [optional] [readonly] 
**paymentCardSchemes** | [**[PaymentCardBrand]**](PaymentCardBrand.md) | Accepted payment card brands. | [optional] 
**reconciliationWindowEnabled** | **Boolean** | If a transaction is not reconciled within the &#x60;reconciliationWindowTtl&#x60; time, then the transaction is marked as &#x60;abandoned&#x60;. | [optional] [default to false]
**reconciliationWindowTtl** | **Number** | The time window (in seconds) allotted for a reconciliation to occur. If it is not reconciled in that time, then the transaction is marked as &#x60;abandoned&#x60;. | [optional] 
**status** | **String** | The gateway account&#39;s status. | [optional] [readonly] 
**sticky** | **Boolean** | Customer&#39;s payment instrument will \&quot;stick\&quot; to the gateway account for future transactions when enabled. | [optional] [default to true]
**threeDSecure** | **Boolean** | True, if Gateway Account allows 3DSecure. | [optional] [default to false]
**timeout** | **Number** | Gateway Account request timeout in seconds. | [optional] 
**token** | **String** | Gateway Account token. | [optional] [readonly] 
**updatedTime** | **Date** | Gateway Account updated time. | [optional] [readonly] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `pending` (value: `"pending"`)

* `closed` (value: `"closed"`)




