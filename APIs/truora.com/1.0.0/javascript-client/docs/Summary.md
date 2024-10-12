# ChecksApi.Summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateOfBirth** | **Date** | Person date of birth in RFC3339 format | [optional] 
**deathDate** | **Date** | Person date of death | [optional] 
**driversLicense** | **String** | Person driver&#39;s license | [optional] 
**gender** | **String** | Person gender | [optional] 
**identityStatus** | **String** | Indicates whether a person was found, found as dead or not found at all | [optional] 
**namesFound** | [**[NameFound]**](NameFound.md) | Names found during the background check process | 
**nss** | **String** | Social security number of the person (Mexico) | [optional] 
**rfc** | **String** | Federal taxpayer registration number of the person | [optional] 



## Enum: GenderEnum


* `male` (value: `"male"`)

* `female` (value: `"female"`)





## Enum: IdentityStatusEnum


* `found` (value: `"found"`)

* `not_found` (value: `"not_found"`)

* `dead` (value: `"dead"`)




