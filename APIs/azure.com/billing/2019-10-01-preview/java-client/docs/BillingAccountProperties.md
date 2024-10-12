

# BillingAccountProperties

The properties of the billing account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**AddressDetails**](AddressDetails.md) |  |  [optional] |
|**agreementType** | [**AgreementTypeEnum**](#AgreementTypeEnum) | The type of agreement. |  [optional] [readonly] |
|**billingProfiles** | [**List&lt;BillingProfile&gt;**](BillingProfile.md) | The billing profiles associated to the billing account. By default this is not populated, unless it&#39;s specified in $expand. |  [optional] |
|**customerType** | [**CustomerTypeEnum**](#CustomerTypeEnum) | The type of customer. |  [optional] [readonly] |
|**departments** | [**List&lt;Department&gt;**](Department.md) | The departments associated to the enrollment. |  [optional] |
|**displayName** | **String** | The billing account name. |  [optional] [readonly] |
|**enrollmentAccounts** | [**List&lt;EnrollmentAccount&gt;**](EnrollmentAccount.md) | The accounts associated to the enrollment. |  [optional] |
|**enrollmentDetails** | [**Enrollment**](Enrollment.md) |  |  [optional] |
|**organizationId** | **String** | Organization id. |  [optional] [readonly] |



## Enum: AgreementTypeEnum

| Name | Value |
|---- | -----|
| MICROSOFT_CUSTOMER_AGREEMENT | &quot;MicrosoftCustomerAgreement&quot; |
| ENTERPRISE_AGREEMENT | &quot;EnterpriseAgreement&quot; |
| MICROSOFT_ONLINE_SERVICES_PROGRAM | &quot;MicrosoftOnlineServicesProgram&quot; |
| MICROSOFT_PARTNER_AGREEMENT | &quot;MicrosoftPartnerAgreement&quot; |



## Enum: CustomerTypeEnum

| Name | Value |
|---- | -----|
| ENTERPRISE | &quot;Enterprise&quot; |
| INDIVIDUAL | &quot;Individual&quot; |
| PARTNER | &quot;Partner&quot; |



