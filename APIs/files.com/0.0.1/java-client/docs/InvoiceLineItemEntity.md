

# InvoiceLineItemEntity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | Invoice line item amount |  [optional] |
|**createdAt** | **OffsetDateTime** | Invoice line item created at date/time |  [optional] |
|**description** | **String** | Invoice line item description |  [optional] |
|**plan** | **String** | Plan name |  [optional] |
|**serviceEndAt** | **OffsetDateTime** | Invoice line item service end date/time |  [optional] |
|**serviceStartAt** | **OffsetDateTime** | Invoice line item service start date/time |  [optional] |
|**site** | **String** | Site name |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Invoice line item type |  [optional] |
|**updatedAt** | **OffsetDateTime** | Invoice line item updated date/time |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INVOICE | &quot;invoice&quot; |
| INVOICE_ADJUSTMENT | &quot;invoice_adjustment&quot; |
| USAGE_OVERAGE | &quot;usage_overage&quot; |
| USER_OVERAGE | &quot;user_overage&quot; |
| ADDON_SUBSCRIPTION | &quot;addon_subscription&quot; |
| MISC_FEE | &quot;misc_fee&quot; |
| USAGE_OVERAGE_ADJUSTMENT | &quot;usage_overage_adjustment&quot; |
| USER_OVERAGE_ADJUSTMENT | &quot;user_overage_adjustment&quot; |
| ADDON_SUBSCRIPTION_ADJUSTMENT | &quot;addon_subscription_adjustment&quot; |
| MISC_FEE_ADJUSTMENT | &quot;misc_fee_adjustment&quot; |
| CREDIT_EXPIRATION | &quot;credit_expiration&quot; |



