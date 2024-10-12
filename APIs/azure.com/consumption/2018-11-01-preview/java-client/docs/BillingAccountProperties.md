

# BillingAccountProperties

The properties of the billing account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The billing account Type. |  [optional] [readonly] |
|**address** | [**Address**](Address.md) |  |  [optional] |
|**agreements** | **String** | Agreements associated with billing account |  [optional] [readonly] |
|**billingProfiles** | [**List&lt;BillingProfile&gt;**](BillingProfile.md) | The billing profiles associated to the billing account. |  [optional] [readonly] |
|**company** | **String** | The Company this billing account belongs to. |  [optional] [readonly] |
|**country** | **String** | The country associated with billing account. |  [optional] [readonly] |
|**defaultCurrency** | **String** | The ISO currency, for example, USD. |  [optional] [readonly] |
|**departments** | [**List&lt;Department&gt;**](Department.md) | The departments associated to the enrollment. |  [optional] [readonly] |
|**enrollmentAccounts** | [**List&lt;EnrollmentAccount&gt;**](EnrollmentAccount.md) | The accounts associated to the enrollment. |  [optional] [readonly] |
|**enrollmentDetails** | [**Enrollment**](Enrollment.md) |  |  [optional] |
|**invoiceSections** | [**List&lt;InvoiceSection&gt;**](InvoiceSection.md) | The invoiceSections associated to the billing account. |  [optional] [readonly] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| COMMERCE_ROOT | &quot;CommerceRoot&quot; |
| ENROLLMENT | &quot;Enrollment&quot; |



