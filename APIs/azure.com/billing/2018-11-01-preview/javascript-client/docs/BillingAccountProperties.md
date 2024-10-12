# BillingManagementClient.BillingAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | The billing account Type. | [optional] [readonly] 
**address** | [**Address**](Address.md) |  | [optional] 
**billingProfiles** | [**[BillingProfile]**](BillingProfile.md) | The billing profiles associated to the billing account. By default this is not populated, unless it&#39;s specified in $expand. | [optional] 
**company** | **String** | Company Name. | [optional] [readonly] 
**country** | **String** | Country Name. | [optional] [readonly] 
**departments** | [**[Department]**](Department.md) | The departments associated to the enrollment. | [optional] 
**displayName** | **String** | The billing account name. | [optional] [readonly] 
**enrollmentAccounts** | [**[EnrollmentAccount]**](EnrollmentAccount.md) | The accounts associated to the enrollment. | [optional] 
**enrollmentDetails** | [**Enrollment**](Enrollment.md) |  | [optional] 
**hasReadAccess** | **Boolean** | Specifies whether the user has read access on billing account. | [optional] [readonly] 
**invoiceSections** | [**[InvoiceSection]**](InvoiceSection.md) | The invoice sections associated to the billing account. By default this is not populated, unless it&#39;s specified in $expand. | [optional] 



## Enum: AccountTypeEnum


* `Organization` (value: `"Organization"`)

* `Enrollment` (value: `"Enrollment"`)




