

# BillingProfile

Contains properties of a Campaign Manager Billing Profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consolidatedInvoice** | **Boolean** | Consolidated invoice option for this billing profile. Used to get a single, consolidated invoice across the chosen invoice level. |  [optional] |
|**countryCode** | **String** | Country code of this billing profile.This is a read-only field. |  [optional] |
|**currencyCode** | **String** | Billing currency code in ISO 4217 format.This is a read-only field. |  [optional] |
|**id** | **String** | ID of this billing profile. This is a read-only, auto-generated field. |  [optional] |
|**invoiceLevel** | [**InvoiceLevelEnum**](#InvoiceLevelEnum) | Invoice level for this billing profile. Used to group fees into separate invoices by account, advertiser, or campaign. |  [optional] |
|**isDefault** | **Boolean** | True if the billing profile is the account default profile. This is a read-only field. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#billingProfile\&quot;. |  [optional] |
|**name** | **String** | Name of this billing profile. This is a required field and must be less than 256 characters long and must be unique among billing profile in the same account. |  [optional] |
|**paymentsAccountId** | **String** | The ID of the payment account the billing profile belongs to. This is a read-only field. |  [optional] |
|**paymentsCustomerId** | **String** | The ID of the payment customer the billing profile belongs to. This is a read-only field. |  [optional] |
|**purchaseOrder** | **String** | Purchase order (PO) for this billing profile. This PO number is used in the invoices for all of the advertisers in this billing profile. |  [optional] |
|**secondaryPaymentsCustomerId** | **String** | The ID of the secondary payment customer the billing profile belongs to. This is a read-only field. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of this billing profile.This is a read-only field. |  [optional] |



## Enum: InvoiceLevelEnum

| Name | Value |
|---- | -----|
| ACCOUNT_LEVEL | &quot;ACCOUNT_LEVEL&quot; |
| ADVERTISER_LEVEL | &quot;ADVERTISER_LEVEL&quot; |
| CAMPAIGN_LEVEL | &quot;CAMPAIGN_LEVEL&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNDER_REVIEW | &quot;UNDER_REVIEW&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |



