

# Behavior

Represents behaviour reports

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**birthDate** | **LocalDate** | Birth date of reported person |  |
|**country** | [**CountryEnum**](#CountryEnum) | Document country |  |
|**creationDate** | **OffsetDateTime** | Feedback creation date |  [optional] |
|**documentId** | **String** | Person document ID |  |
|**documentType** | [**DocumentTypeEnum**](#DocumentTypeEnum) | Document type associated with the background check |  |
|**email** | **String** | Reported person e-mail |  |
|**feedbackDate** | **LocalDate** | Behavior report date |  |
|**firstName** | **String** | Person first name |  |
|**lastName** | **String** | Person last name |  |
|**phoneNumber** | **String** | Phone number of the reported person |  [optional] |
|**reason** | **String** | Report reason |  |



## Enum: CountryEnum

| Name | Value |
|---- | -----|
| CO | &quot;co&quot; |
| VE | &quot;ve&quot; |
| CL | &quot;cl&quot; |
| MX | &quot;mx&quot; |
| PE | &quot;pe&quot; |
| DO | &quot;do&quot; |
| SV | &quot;sv&quot; |
| GT | &quot;gt&quot; |
| BO | &quot;bo&quot; |
| CR | &quot;cr&quot; |
| EC | &quot;ec&quot; |
| PA | &quot;pa&quot; |
| BR | &quot;br&quot; |



## Enum: DocumentTypeEnum

| Name | Value |
|---- | -----|
| NATIONAL_ID | &quot;national-id&quot; |
| PASSPORT | &quot;passport&quot; |
| FOREIGN_ID | &quot;foreign-id&quot; |
| NIT | &quot;nit&quot; |
| DIPLOMATIC_ID | &quot;diplomatic-id&quot; |
| CIVIL_REGISTRATION | &quot;civil-registration&quot; |
| IDENTITY_CARD | &quot;identity-card&quot; |
| FOREIGNER_CARD | &quot;foreigner-card&quot; |
| PROFESSIONAL_CARD | &quot;professional-card&quot; |
| MILITARY_CARD | &quot;military-card&quot; |
| PEP | &quot;pep&quot; |
| NIS | &quot;nis&quot; |
| DNI | &quot;dni&quot; |
| RUI | &quot;rui&quot; |
| LICENSE_PLATE | &quot;license-plate&quot; |
| QUERY | &quot;query&quot; |
| NAME | &quot;name&quot; |
| RUT | &quot;rut&quot; |
| NUIP | &quot;nuip&quot; |
| FOREIGN_SOCIETIES | &quot;foreign-societies&quot; |
| ESCROW | &quot;escrow&quot; |
| INDIVIDUAL_REGISTRATION | &quot;individual-registration&quot; |
| GENERAL_REGISTRATION | &quot;general-registration&quot; |
| CURP | &quot;curp&quot; |
| DUI | &quot;dui&quot; |
| DRIVER_LICENSE | &quot;driver-license&quot; |
| RUC | &quot;ruc&quot; |



