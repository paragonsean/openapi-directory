# FirebaseHostingApi.Domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainName** | **String** | Required. The domain name of the association. | [optional] 
**domainRedirect** | [**DomainRedirect**](DomainRedirect.md) |  | [optional] 
**provisioning** | [**DomainProvisioning**](DomainProvisioning.md) |  | [optional] 
**site** | **String** | Required. The site name of the association. | [optional] 
**status** | **String** | Output only. Additional status of the domain association. | [optional] 
**updateTime** | **String** | Output only. The time at which the domain was last updated. | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"DOMAIN_STATUS_UNSPECIFIED"`)

* `CHANGE_PENDING` (value: `"DOMAIN_CHANGE_PENDING"`)

* `ACTIVE` (value: `"DOMAIN_ACTIVE"`)

* `VERIFICATION_REQUIRED` (value: `"DOMAIN_VERIFICATION_REQUIRED"`)

* `VERIFICATION_LOST` (value: `"DOMAIN_VERIFICATION_LOST"`)




