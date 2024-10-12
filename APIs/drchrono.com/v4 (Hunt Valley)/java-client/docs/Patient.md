

# Patient


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** |  |  [optional] |
|**autoAccidentInsurance** | [**AutoAccidentInsurance**](AutoAccidentInsurance.md) |  |  [optional] |
|**cellPhone** | **String** |  |  [optional] |
|**chartId** | **String** | Automatically set using first &amp; last name if absent |  [optional] |
|**city** | **String** |  |  [optional] |
|**copay** | **String** |  |  [optional] |
|**customDemographics** | [**List&lt;CustomPatientFieldValue&gt;**](CustomPatientFieldValue.md) |  |  [optional] |
|**dateOfBirth** | **String** |  |  [optional] |
|**dateOfFirstAppointment** | **String** | Date of first patient visit. |  [optional] |
|**dateOfLastAppointment** | **String** | Date of previous patient visit |  [optional] |
|**defaultPharmacy** | **String** | ncpdp id of patient&#39;s default pharmacy |  [optional] |
|**disableSmsMessages** | **Boolean** | If True, suppress SMS/Txt messages to this patient even if we have a cell phone # for them. |  [optional] |
|**doctor** | **Integer** |  |  |
|**email** | **String** |  |  [optional] |
|**emergencyContactName** | **String** |  |  [optional] |
|**emergencyContactPhone** | **String** |  |  [optional] |
|**emergencyContactRelation** | **String** |  |  [optional] |
|**employer** | **String** |  |  [optional] |
|**employerAddress** | **String** |  |  [optional] |
|**employerCity** | **String** |  |  [optional] |
|**employerState** | **String** | Two-letter abbreviation |  [optional] |
|**employerZipCode** | **String** |  |  [optional] |
|**ethnicity** | [**EthnicityEnum**](#EthnicityEnum) | One of &#x60;\&quot;blank\&quot;&#x60;, &#x60;\&quot;hispanic\&quot;&#x60;, &#x60;\&quot;not_hispanic\&quot;&#x60; or &#x60;\&quot;declined\&quot;&#x60; |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | One of &#x60;\&quot;Male\&quot;&#x60;, &#x60;\&quot;Female\&quot;&#x60;, or &#x60;\&quot;Other\&quot;&#x60; |  |
|**homePhone** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastName** | **String** |  |  [optional] |
|**middleName** | **String** |  |  [optional] |
|**nickName** | **String** | Common name for patient, should be used instead of first name if supplied. |  [optional] |
|**officePhone** | **String** |  |  [optional] |
|**offices** | **List&lt;Integer&gt;** | IDs of every office this patient has been to |  [optional] |
|**patientFlags** | [**List&lt;PatientFlagType1&gt;**](PatientFlagType1.md) | Possible patient flag type that can be attached to the patient |  [optional] [readonly] |
|**patientFlagsAttached** | [**List&lt;PatientFlag&gt;**](PatientFlag.md) | Patient flags attached to the patient |  [optional] |
|**patientPaymentProfile** | [**PatientPaymentProfileEnum**](#PatientPaymentProfileEnum) | One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Cash\&quot;&#x60;, &#x60;\&quot;Insurance\&quot;&#x60;, &#x60;\&quot;Insurance Out of Network\&quot;&#x60;, &#x60;\&quot;Auto Accident\&quot;&#x60; or &#x60;\&quot;Worker&#39;s Comp\&quot;&#x60;.&lt;br&gt;**Note:** Patient must already have either &#x60;primary_insurance&#x60; or &#x60;secondary_insurance&#x60; or new &#x60;primary_insurance&#x60; or &#x60;secondary_insurance&#x60; is passed in request if &#x60;Insurance&#x60;, &#x60;Auto Accident&#x60; or &#x60;Worker&#39;s Comp&#x60; payment profiles are chosen. |  [optional] |
|**patientPhoto** | **String** |  |  [optional] |
|**patientPhotoDate** | **String** | Cannot be passed without &#x60;patient_photo&#x60; |  [optional] |
|**patientStatus** | [**PatientStatusEnum**](#PatientStatusEnum) | One of &#x60;\&quot;A\&quot;&#x60; (active), &#x60;\&quot;I\&quot;&#x60; (inactive), &#x60;\&quot;D\&quot;&#x60; (inactive-deceased) |  [optional] |
|**preferredLanguage** | [**PreferredLanguageEnum**](#PreferredLanguageEnum) | Use ISO 639 alpha-3 codes |  [optional] |
|**primaryCarePhysician** | **String** | Referring doctor for this patient |  [optional] |
|**primaryInsurance** | [**PrimaryInsurance**](PrimaryInsurance.md) |  |  [optional] |
|**race** | [**RaceEnum**](#RaceEnum) | One of &#x60;\&quot;blank\&quot;&#x60;, &#x60;\&quot;indian\&quot;&#x60;, &#x60;\&quot;asian\&quot;&#x60;, &#x60;\&quot;black\&quot;&#x60;, &#x60;\&quot;hawaiian\&quot;&#x60;, &#x60;\&quot;white\&quot;&#x60; or &#x60;\&quot;declined\&quot;&#x60; |  [optional] |
|**referringDoctor** | [**Patient1**](Patient1.md) |  |  [optional] |
|**referringSource** | **String** | Referring source. |  [optional] |
|**responsiblePartyEmail** | **String** |  |  [optional] |
|**responsiblePartyName** | **String** |  |  [optional] |
|**responsiblePartyPhone** | **String** |  |  [optional] |
|**responsiblePartyRelation** | **String** |  |  [optional] |
|**secondaryInsurance** | [**SecondaryInsurance**](SecondaryInsurance.md) |  |  [optional] |
|**socialSecurityNumber** | **String** |  |  [optional] |
|**state** | **String** | Two-letter abbreviation |  [optional] |
|**tertiaryInsurance** | [**TertiaryInsurance**](TertiaryInsurance.md) |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |
|**workersCompInsurance** | [**WorkerCompInsurance**](WorkerCompInsurance.md) |  |  [optional] |
|**zipCode** | **String** |  |  [optional] |



## Enum: EthnicityEnum

| Name | Value |
|---- | -----|
| BLANK | &quot;blank&quot; |
| HISPANIC | &quot;hispanic&quot; |
| NOT_HISPANIC | &quot;not_hispanic&quot; |
| DECLINED | &quot;declined&quot; |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| MALE | &quot;Male&quot; |
| FEMALE | &quot;Female&quot; |
| OTHER | &quot;Other&quot; |
| UNK | &quot;UNK&quot; |
| ASKU | &quot;ASKU&quot; |



## Enum: PatientPaymentProfileEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| CASH | &quot;Cash&quot; |
| INSURANCE | &quot;Insurance&quot; |
| INSURANCE_OUT_OF_NETWORK | &quot;Insurance Out of Network&quot; |
| AUTO_ACCIDENT | &quot;Auto Accident&quot; |
| WORKER_S_COMP | &quot;Worker&#39;s Comp&quot; |



## Enum: PatientStatusEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| I | &quot;I&quot; |
| D | &quot;D&quot; |



## Enum: PreferredLanguageEnum

| Name | Value |
|---- | -----|
| BLANK | &quot;blank&quot; |
| ENG | &quot;eng&quot; |
| ZHO | &quot;zho&quot; |
| FRA | &quot;fra&quot; |
| ITA | &quot;ita&quot; |
| JPN | &quot;jpn&quot; |
| POR | &quot;por&quot; |
| RUS | &quot;rus&quot; |
| SPA | &quot;spa&quot; |
| OTHER | &quot;other&quot; |
| UNKNOWN | &quot;unknown&quot; |
| DECLINED | &quot;declined&quot; |



## Enum: RaceEnum

| Name | Value |
|---- | -----|
| BLANK | &quot;blank&quot; |
| INDIAN | &quot;indian&quot; |
| ASIAN | &quot;asian&quot; |
| BLACK | &quot;black&quot; |
| HAWAIIAN | &quot;hawaiian&quot; |
| WHITE | &quot;white&quot; |
| OTHER | &quot;other&quot; |
| DECLINED | &quot;declined&quot; |



