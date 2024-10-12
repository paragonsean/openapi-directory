

# PatientVaccineRecord


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**administeredAt** | **Integer** | ID of &#x60;/api/offices&#x60; where the administration happened |  [optional] |
|**administeredBy** | **String** | ID of &#x60;/api/users&#x60; who performs the administration |  [optional] |
|**administrationStart** | **String** | Datetime when the administration starts |  [optional] |
|**amount** | **BigDecimal** | Amount of vaccine administered |  [optional] |
|**comments** | **String** |  |  [optional] |
|**completionStatus** | [**CompletionStatusEnum**](#CompletionStatusEnum) | Vaccination status, can be &#x60;CP&#x60;(Complete), &#x60;RE&#x60;(Refused), &#x60;NA&#x60;(Not administered), &#x60;PA&#x60;(Partially administered) |  [optional] |
|**consentForm** | **Integer** | Consent form related with vaccine record |  [optional] |
|**cptCode** | **String** | Vaccine cpt code |  [optional] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**cvxCode** | **String** | Vaccine cvx code |  |
|**doses** | [**List&lt;VaccineDose&gt;**](VaccineDose.md) | Vaccine dose IDs received in consent form signed hook |  [optional] |
|**enteredBy** | **String** | ID of user who created the record |  [optional] [readonly] |
|**fundingEligibility** | [**FundingEligibilityEnum**](#FundingEligibilityEnum) | The funding program that should pay for a given immunization |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**nextDoseDate** | **String** | Date for next dose of vaccine |  [optional] |
|**observedImmunity** | [**ObservedImmunityEnum**](#ObservedImmunityEnum) |  |  [optional] |
|**orderingDoctor** | **Integer** |  |  [optional] |
|**patient** | **Integer** |  |  |
|**recordSource** | [**RecordSourceEnum**](#RecordSourceEnum) |  |  [optional] |
|**route** | **String** |  |  [optional] |
|**site** | **String** |  |  [optional] |
|**units** | **String** |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |
|**vaccineInventory** | **Integer** | ID of &#x60;/api/vaccine_inventories&#x60; the vaccine is from |  [optional] |
|**vis** | **String** | Related vaccine information statement |  [optional] [readonly] |



## Enum: CompletionStatusEnum

| Name | Value |
|---- | -----|
| CP | &quot;CP&quot; |
| RE | &quot;RE&quot; |
| NA | &quot;NA&quot; |
| PA | &quot;PA&quot; |



## Enum: FundingEligibilityEnum

| Name | Value |
|---- | -----|
| V01 | &quot;V01&quot; |
| V02 | &quot;V02&quot; |
| V03 | &quot;V03&quot; |
| V04 | &quot;V04&quot; |
| V05 | &quot;V05&quot; |
| V07 | &quot;V07&quot; |



## Enum: ObservedImmunityEnum

| Name | Value |
|---- | -----|
| _398102009 | &quot;398102009&quot; |
| _409498004 | &quot;409498004&quot; |
| _397428000 | &quot;397428000&quot; |
| _18624000 | &quot;18624000&quot; |
| _91428005 | &quot;91428005&quot; |
| _271511000 | &quot;271511000&quot; |
| _240532009 | &quot;240532009&quot; |
| _6142004 | &quot;6142004&quot; |
| _52947006 | &quot;52947006&quot; |
| _14189004 | &quot;14189004&quot; |
| _23511006 | &quot;23511006&quot; |
| _36989005 | &quot;36989005&quot; |
| _27836007 | &quot;27836007&quot; |
| _16814004 | &quot;16814004&quot; |
| _14168008 | &quot;14168008&quot; |
| _36653000 | &quot;36653000&quot; |
| _76902006 | &quot;76902006&quot; |
| _66071002 | &quot;66071002&quot; |
| _4834000 | &quot;4834000&quot; |
| _111852003 | &quot;111852003&quot; |
| _38907003 | &quot;38907003&quot; |
| _40468003 | &quot;40468003&quot; |
| _16541001 | &quot;16541001&quot; |



## Enum: RecordSourceEnum

| Name | Value |
|---- | -----|
| _00 | &quot;00&quot; |
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |
| _06 | &quot;06&quot; |
| _07 | &quot;07&quot; |
| _08 | &quot;08&quot; |



