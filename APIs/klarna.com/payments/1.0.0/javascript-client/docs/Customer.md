# KlarnaPaymentsApiV1.Customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateOfBirth** | **String** | Customer’s date of birth. The format is ‘yyyy-mm-dd’ | [optional] 
**gender** | **String** | Customer’s gender - ‘male’ or ‘female’ | [optional] 
**lastFourSsn** | **String** | Last four digits of the customer&#39;s social security number. This value is available for US customers. | [optional] 
**nationalIdentificationNumber** | **String** | The customer&#39;s national identification number. This value is available for EU customers utilizing national identification numbers. | [optional] 
**organizationEntityType** | **String** | Organization entity type. Only applicable for B2B customers. | [optional] 
**organizationRegistrationId** | **String** | Organization registration id. Only applicable for B2B customers. | [optional] 
**title** | **String** | Customer’s Title. Allowed values per country: UK - \&quot;Mr\&quot;, \&quot;Ms\&quot; DE - \&quot;Herr\&quot;, \&quot;Frau\&quot; AT: \&quot;Herr, \&quot;Frau\&quot; CH: de-CH: \&quot;Herr, \&quot;Frau\&quot; it-CH: \&quot;Sig.\&quot;, \&quot;Sig.ra\&quot; fr-CH: \&quot;M\&quot;, \&quot;Mme\&quot;  BE: \&quot;Dhr.\&quot;, \&quot;Mevr.\&quot; NL: \&quot;Dhr.\&quot;, \&quot;Mevr.\&quot; | [optional] 
**type** | **String** | Type of customer in the session. If nothing is added, a B2C session will be the default. If it is a b2b-session, you should enter organization to trigger a B2B session. | [optional] 
**vatId** | **String** | VAT ID. Only applicable for B2B customers. | [optional] 



## Enum: OrganizationEntityTypeEnum


* `LIMITED_COMPANY` (value: `"LIMITED_COMPANY"`)

* `PUBLIC_LIMITED_COMPANY` (value: `"PUBLIC_LIMITED_COMPANY"`)

* `ENTREPRENEURIAL_COMPANY` (value: `"ENTREPRENEURIAL_COMPANY"`)

* `LIMITED_PARTNERSHIP_LIMITED_COMPANY` (value: `"LIMITED_PARTNERSHIP_LIMITED_COMPANY"`)

* `LIMITED_PARTNERSHIP` (value: `"LIMITED_PARTNERSHIP"`)

* `GENERAL_PARTNERSHIP` (value: `"GENERAL_PARTNERSHIP"`)

* `REGISTERED_SOLE_TRADER` (value: `"REGISTERED_SOLE_TRADER"`)

* `SOLE_TRADER` (value: `"SOLE_TRADER"`)

* `CIVIL_LAW_PARTNERSHIP` (value: `"CIVIL_LAW_PARTNERSHIP"`)

* `PUBLIC_INSTITUTION` (value: `"PUBLIC_INSTITUTION"`)

* `OTHER` (value: `"OTHER"`)




