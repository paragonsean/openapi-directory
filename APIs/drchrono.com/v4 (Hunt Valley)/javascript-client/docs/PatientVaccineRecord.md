# OpenapiJsClient.PatientVaccineRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administeredAt** | **Number** | ID of &#x60;/api/offices&#x60; where the administration happened | [optional] 
**administeredBy** | **String** | ID of &#x60;/api/users&#x60; who performs the administration | [optional] 
**administrationStart** | **String** | Datetime when the administration starts | [optional] 
**amount** | **Number** | Amount of vaccine administered | [optional] 
**comments** | **String** |  | [optional] 
**completionStatus** | **String** | Vaccination status, can be &#x60;CP&#x60;(Complete), &#x60;RE&#x60;(Refused), &#x60;NA&#x60;(Not administered), &#x60;PA&#x60;(Partially administered) | [optional] 
**consentForm** | **Number** | Consent form related with vaccine record | [optional] 
**cptCode** | **String** | Vaccine cpt code | [optional] 
**createdAt** | **String** |  | [optional] [readonly] 
**cvxCode** | **String** | Vaccine cvx code | 
**doses** | [**[VaccineDose]**](VaccineDose.md) | Vaccine dose IDs received in consent form signed hook | [optional] 
**enteredBy** | **String** | ID of user who created the record | [optional] [readonly] 
**fundingEligibility** | **String** | The funding program that should pay for a given immunization | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**name** | **String** |  | 
**nextDoseDate** | **String** | Date for next dose of vaccine | [optional] 
**observedImmunity** | **String** |  | [optional] 
**orderingDoctor** | **Number** |  | [optional] 
**patient** | **Number** |  | 
**recordSource** | **String** |  | [optional] 
**route** | **String** |  | [optional] 
**site** | **String** |  | [optional] 
**units** | **String** |  | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 
**vaccineInventory** | **Number** | ID of &#x60;/api/vaccine_inventories&#x60; the vaccine is from | [optional] 
**vis** | **String** | Related vaccine information statement | [optional] [readonly] 



## Enum: CompletionStatusEnum


* `CP` (value: `"CP"`)

* `RE` (value: `"RE"`)

* `NA` (value: `"NA"`)

* `PA` (value: `"PA"`)





## Enum: FundingEligibilityEnum


* `V01` (value: `"V01"`)

* `V02` (value: `"V02"`)

* `V03` (value: `"V03"`)

* `V04` (value: `"V04"`)

* `V05` (value: `"V05"`)

* `V07` (value: `"V07"`)





## Enum: ObservedImmunityEnum


* `398102009` (value: `"398102009"`)

* `409498004` (value: `"409498004"`)

* `397428000` (value: `"397428000"`)

* `18624000` (value: `"18624000"`)

* `91428005` (value: `"91428005"`)

* `271511000` (value: `"271511000"`)

* `240532009` (value: `"240532009"`)

* `6142004` (value: `"6142004"`)

* `52947006` (value: `"52947006"`)

* `14189004` (value: `"14189004"`)

* `23511006` (value: `"23511006"`)

* `36989005` (value: `"36989005"`)

* `27836007` (value: `"27836007"`)

* `16814004` (value: `"16814004"`)

* `14168008` (value: `"14168008"`)

* `36653000` (value: `"36653000"`)

* `76902006` (value: `"76902006"`)

* `66071002` (value: `"66071002"`)

* `4834000` (value: `"4834000"`)

* `111852003` (value: `"111852003"`)

* `38907003` (value: `"38907003"`)

* `40468003` (value: `"40468003"`)

* `16541001` (value: `"16541001"`)





## Enum: RecordSourceEnum


* `00` (value: `"00"`)

* `01` (value: `"01"`)

* `02` (value: `"02"`)

* `03` (value: `"03"`)

* `04` (value: `"04"`)

* `05` (value: `"05"`)

* `06` (value: `"06"`)

* `07` (value: `"07"`)

* `08` (value: `"08"`)




