

# BillingAccountProperties

The properties of the billing account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The billing account Type. |  [optional] [readonly] |
|**address** | [**Address**](Address.md) |  |  [optional] |
|**billingProfiles** | [**List&lt;BillingProfile&gt;**](BillingProfile.md) | The billing profiles associated to the billing account. By default this is not populated, unless it&#39;s specified in $expand. |  [optional] |
|**company** | **String** | Company Name. |  [optional] [readonly] |
|**country** | **String** | Country Name. |  [optional] [readonly] |
|**departments** | [**List&lt;Department&gt;**](Department.md) | The departments associated to the enrollment. |  [optional] |
|**displayName** | **String** | The billing account name. |  [optional] [readonly] |
|**enrollmentAccounts** | [**List&lt;EnrollmentAccount&gt;**](EnrollmentAccount.md) | The accounts associated to the enrollment. |  [optional] |
|**enrollmentDetails** | [**Enrollment**](Enrollment.md) |  |  [optional] |
|**hasReadAccess** | **Boolean** | Specifies whether the user has read access on billing account. |  [optional] [readonly] |
|**invoiceSections** | [**List&lt;InvoiceSection&gt;**](InvoiceSection.md) | The invoice sections associated to the billing account. By default this is not populated, unless it&#39;s specified in $expand. |  [optional] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| ORGANIZATION | &quot;Organization&quot; |
| ENROLLMENT | &quot;Enrollment&quot; |



