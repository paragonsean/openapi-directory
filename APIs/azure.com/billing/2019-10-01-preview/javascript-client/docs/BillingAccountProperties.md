# BillingManagementClient.BillingAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddressDetails**](AddressDetails.md) |  | [optional] 
**agreementType** | **String** | The type of agreement. | [optional] [readonly] 
**billingProfiles** | [**[BillingProfile]**](BillingProfile.md) | The billing profiles associated to the billing account. By default this is not populated, unless it&#39;s specified in $expand. | [optional] 
**customerType** | **String** | The type of customer. | [optional] [readonly] 
**departments** | [**[Department]**](Department.md) | The departments associated to the enrollment. | [optional] 
**displayName** | **String** | The billing account name. | [optional] [readonly] 
**enrollmentAccounts** | [**[EnrollmentAccount]**](EnrollmentAccount.md) | The accounts associated to the enrollment. | [optional] 
**enrollmentDetails** | [**Enrollment**](Enrollment.md) |  | [optional] 
**organizationId** | **String** | Organization id. | [optional] [readonly] 



## Enum: AgreementTypeEnum


* `MicrosoftCustomerAgreement` (value: `"MicrosoftCustomerAgreement"`)

* `EnterpriseAgreement` (value: `"EnterpriseAgreement"`)

* `MicrosoftOnlineServicesProgram` (value: `"MicrosoftOnlineServicesProgram"`)

* `MicrosoftPartnerAgreement` (value: `"MicrosoftPartnerAgreement"`)





## Enum: CustomerTypeEnum


* `Enterprise` (value: `"Enterprise"`)

* `Individual` (value: `"Individual"`)

* `Partner` (value: `"Partner"`)




