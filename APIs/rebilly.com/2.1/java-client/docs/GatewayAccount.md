

# GatewayAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;GatewayAccountLinksInner&gt;**](GatewayAccountLinksInner.md) | The links related to resource. |  [optional] [readonly] |
|**acceptedCurrencies** | **List&lt;String&gt;** | Accepted currencies (array of the currency three letter codes). |  |
|**acquirerName** | **AcquirerName** |  |  [optional] |
|**additionalFilters** | **String** | The additional filters are used to determine whether the gateway account can be selected for the transaction to be processed. For example, the filter may put a maximum amount value. If the transaction is above that amount, this gateway account wouldn&#39;t be used. This follows our standard filter format.  |  [optional] |
|**approvalWindowTtl** | **Integer** | The time window (in seconds) allotted for approving an offsite transaction before it is automatically &#x60;abandoned&#x60;. |  [optional] |
|**cityField** | **String** | The gateway account&#39;s city field (also known as line 2 descriptor). |  [optional] |
|**createdTime** | **OffsetDateTime** | Gateway Account created time. |  [optional] [readonly] |
|**dccForceCurrency** | **String** | Force dynamic currency conversion to the specified currency on each sale. Leave it empty to disable force DCC.  |  [optional] |
|**dccMarkup** | **Integer** | Dynamic currency conversion markup in basis points. |  [optional] |
|**descriptor** | **String** | The gateway account&#39;s descriptor. |  [optional] |
|**digitalWallets** | [**DigitalWallets**](DigitalWallets.md) |  |  [optional] |
|**dynamicDescriptor** | **Boolean** | True, if Gateway Account allows dynamic descriptor. |  [optional] |
|**excludedDccQuoteCurrencies** | **List&lt;String&gt;** | Excluded Dynamic Currency Conversion Quote Currencies. |  [optional] |
|**gatewayName** | **GatewayName** |  |  |
|**id** | **String** | The gateway identifier string. |  [optional] [readonly] |
|**isDown** | **Boolean** | True if gateway is currently in downtime period. |  [optional] [readonly] |
|**merchantCategoryCode** | **String** | The gateway account&#39;s merchant category code. |  [optional] |
|**method** | **PaymentMethod** |  |  |
|**monthlyLimit** | **Double** | Monthly Limit. |  [optional] |
|**organizationId** | **String** | Organization ID. |  [optional] [readonly] |
|**paymentCardSchemes** | **List&lt;PaymentCardBrand&gt;** | Accepted payment card brands. |  [optional] |
|**reconciliationWindowEnabled** | **Boolean** | If a transaction is not reconciled within the &#x60;reconciliationWindowTtl&#x60; time, then the transaction is marked as &#x60;abandoned&#x60;. |  [optional] |
|**reconciliationWindowTtl** | **Integer** | The time window (in seconds) allotted for a reconciliation to occur. If it is not reconciled in that time, then the transaction is marked as &#x60;abandoned&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The gateway account&#39;s status. |  [optional] [readonly] |
|**sticky** | **Boolean** | Customer&#39;s payment instrument will \&quot;stick\&quot; to the gateway account for future transactions when enabled. |  [optional] |
|**threeDSecure** | **Boolean** | True, if Gateway Account allows 3DSecure. |  [optional] |
|**timeout** | **Integer** | Gateway Account request timeout in seconds. |  [optional] |
|**token** | **String** | Gateway Account token. |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | Gateway Account updated time. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| PENDING | &quot;pending&quot; |
| CLOSED | &quot;closed&quot; |



