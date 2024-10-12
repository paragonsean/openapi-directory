

# Summary

Represents a background check summary

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateOfBirth** | **OffsetDateTime** | Person date of birth in RFC3339 format |  [optional] |
|**deathDate** | **OffsetDateTime** | Person date of death |  [optional] |
|**driversLicense** | **String** | Person driver&#39;s license |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | Person gender |  [optional] |
|**identityStatus** | [**IdentityStatusEnum**](#IdentityStatusEnum) | Indicates whether a person was found, found as dead or not found at all |  [optional] |
|**namesFound** | [**List&lt;NameFound&gt;**](NameFound.md) | Names found during the background check process |  |
|**nss** | **String** | Social security number of the person (Mexico) |  [optional] |
|**rfc** | **String** | Federal taxpayer registration number of the person |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |



## Enum: IdentityStatusEnum

| Name | Value |
|---- | -----|
| FOUND | &quot;found&quot; |
| NOT_FOUND | &quot;not_found&quot; |
| DEAD | &quot;dead&quot; |



