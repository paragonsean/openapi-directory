

# CredasApiModelsRegistrationsAddInstantRegistrationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | **String** |  |  |
|**documentParameters** | [**List&lt;CredasApiModelsRegistrationsKeyValueItem&gt;**](CredasApiModelsRegistrationsKeyValueItem.md) |  |  [optional] |
|**documentType** | [**DocumentTypeEnum**](#DocumentTypeEnum) | Other &#x3D; 0, Passport &#x3D; 1, DrivingLicence &#x3D; 2, Visa &#x3D; 3, CscsCard &#x3D; 4, HomeOfficeLetter &#x3D; 5, BirthCertificate &#x3D; 6, NationalIdCard &#x3D; 7, ResidencePermit &#x3D; 9, UtilityBill &#x3D; 11 |  |
|**forename** | **String** |  |  |
|**middleName** | **String** |  |  [optional] |
|**parameters** | [**List&lt;CredasApiModelsRegistrationsKeyValueItem&gt;**](CredasApiModelsRegistrationsKeyValueItem.md) |  |  [optional] |
|**referenceId** | **String** |  |  [optional] |
|**regTypeId** | **UUID** |  |  |
|**selfie** | **String** |  |  [optional] |
|**significantPersonId** | **UUID** |  |  [optional] |
|**surname** | **String** |  |  |



## Enum: DocumentTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |
| NUMBER_9 | 9 |
| NUMBER_10 | 10 |
| NUMBER_11 | 11 |



