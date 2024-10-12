# ConsumptionManagementClient.BillingAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | The billing account Type. | [optional] [readonly] 
**address** | [**Address**](Address.md) |  | [optional] 
**agreements** | **String** | Agreements associated with billing account | [optional] [readonly] 
**billingProfiles** | [**[BillingProfile]**](BillingProfile.md) | The billing profiles associated to the billing account. | [optional] [readonly] 
**company** | **String** | The Company this billing account belongs to. | [optional] [readonly] 
**country** | **String** | The country associated with billing account. | [optional] [readonly] 
**defaultCurrency** | **String** | The ISO currency, for example, USD. | [optional] [readonly] 
**departments** | [**[Department]**](Department.md) | The departments associated to the enrollment. | [optional] [readonly] 
**enrollmentAccounts** | [**[EnrollmentAccount]**](EnrollmentAccount.md) | The accounts associated to the enrollment. | [optional] [readonly] 
**enrollmentDetails** | [**Enrollment**](Enrollment.md) |  | [optional] 
**invoiceSections** | [**[InvoiceSection]**](InvoiceSection.md) | The invoiceSections associated to the billing account. | [optional] [readonly] 



## Enum: AccountTypeEnum


* `CommerceRoot` (value: `"CommerceRoot"`)

* `Enrollment` (value: `"Enrollment"`)




