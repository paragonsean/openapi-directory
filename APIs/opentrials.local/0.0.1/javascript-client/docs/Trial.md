# OpenTrialsApi.Trial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ageRange** | [**TrialAgeRange**](TrialAgeRange.md) |  | [optional] 
**briefSummary** | **String** | Summary of the trial | [optional] 
**completionDate** | **Date** | Date the trial was completed | [optional] 
**conditions** | [**[Condition]**](Condition.md) | Conditions the trial refers to | [optional] 
**discrepancies** | **Object** | Discrepancies in trial&#39;s details between different sources | [optional] 
**documents** | [**[DocumentSummary]**](DocumentSummary.md) | Documents related to the trial | [optional] 
**gender** | **String** | Gender of the subjects of the trial | [optional] 
**hasPublishedResults** | **Boolean** | Trial has its results published (true/false) | [optional] 
**id** | **String** | ID of the trial | 
**identifiers** | **Object** | Object that maps the trial&#39;s sources ids with its identifiers. | [optional] 
**interventions** | [**[Intervention]**](Intervention.md) | Interventions related to the trial | 
**locations** | [**[TrialLocation]**](TrialLocation.md) | Locations related to the trial | 
**organisations** | [**[TrialOrganisation]**](TrialOrganisation.md) | Organisations related to the trial | 
**persons** | [**[TrialPerson]**](TrialPerson.md) | People related to the trial | 
**publicTitle** | **String** | Title of the trial | 
**publications** | [**[PublicationSummary]**](PublicationSummary.md) | Publications referring the trial | 
**records** | [**[RecordSummary]**](RecordSummary.md) | (published) records of the trial | 
**recruitmentStatus** | **String** | Recruitment status of the trial | [optional] 
**registrationDate** | **Date** | Date the trial was registered | [optional] 
**resultsExemptionDate** | **Date** | Date when a certification of exemption has been filed for the trial | [optional] 
**risksOfBias** | [**[RiskOfBias]**](RiskOfBias.md) |  | 
**sourceId** | **String** | ID of the trial&#39;s source | [optional] 
**sources** | **Object** |  | 
**status** | **String** | Completion status of the trial | [optional] 
**studyPhase** | **[String]** | Phases of the study (e.g. &#x60;[\&quot;Phase 2\&quot;]&#x60; or &#x60;[\&quot;Phase 1\&quot;, \&quot;Phase 2\&quot;]&#x60;) | [optional] 
**targetSampleSize** | **Number** | Target sample size for the trial | [optional] 
**url** | **String** | Source URL (where the trial was collected from) | 



## Enum: GenderEnum


* `both` (value: `"both"`)

* `male` (value: `"male"`)

* `female` (value: `"female"`)





## Enum: RecruitmentStatusEnum


* `recruiting` (value: `"recruiting"`)

* `not_recruiting` (value: `"not_recruiting"`)

* `unknown` (value: `"unknown"`)

* `other` (value: `"other"`)





## Enum: StatusEnum


* `ongoing` (value: `"ongoing"`)

* `withdrawn` (value: `"withdrawn"`)

* `suspended` (value: `"suspended"`)

* `terminated` (value: `"terminated"`)

* `complete` (value: `"complete"`)

* `unknown` (value: `"unknown"`)

* `other` (value: `"other"`)




