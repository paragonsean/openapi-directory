

# BillingPlan

Billing Plan

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, Object&gt;** | Collection of attribute values. |  [optional] |
|**id** | **String** | The Billing Plan ID |  [optional] |
|**limits** | **Map&lt;String, BigDecimal&gt;** | A collection of named numeric values |  [optional] |
|**parentId** | **String** |  |  [optional] |
|**paymentSource** | [**PaymentSourceEnum**](#PaymentSourceEnum) | Service that receives payments for this billing plan. |  [optional] |
|**price** | **BigDecimal** | Price of the Billing Plan |  [optional] |
|**service** | [**ServiceEnum**](#ServiceEnum) | Name of the service that the plan applies to. |  [optional] |
|**version** | **String** | Version of the Billing Plan schema |  [optional] |



## Enum: PaymentSourceEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| APP_CENTER | &quot;AppCenter&quot; |
| GIT_HUB | &quot;GitHub&quot; |
| XTC | &quot;Xtc&quot; |



## Enum: ServiceEnum

| Name | Value |
|---- | -----|
| BUILD | &quot;Build&quot; |
| TEST | &quot;Test&quot; |



