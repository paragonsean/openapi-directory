

# CredasApiModelsStatusChecksCompanyDirectorCompanyDirectorResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**companyAppointments** | [**List&lt;CredasApiModelsStatusChecksCompanyDirectorCompanyAppointment&gt;**](CredasApiModelsStatusChecksCompanyDirectorCompanyAppointment.md) |  |  [optional] |
|**companyName** | **String** |  |  [optional] |
|**companyRegNo** | **String** |  |  [optional] |
|**dateAppointed** | **OffsetDateTime** |  |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | Unknown &#x3D; 0, NameAndDateOfBirth &#x3D; 1, NameAndAddress &#x3D; 2, NameAndAddressAndDateOfBirth &#x3D; 3 |  [optional] |
|**matchTypeText** | **String** |  |  [optional] [readonly] |
|**registeredOffice** | **String** |  |  [optional] |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



