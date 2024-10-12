

# Trial


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ageRange** | [**TrialAgeRange**](TrialAgeRange.md) |  |  [optional] |
|**briefSummary** | **String** | Summary of the trial |  [optional] |
|**completionDate** | **OffsetDateTime** | Date the trial was completed |  [optional] |
|**conditions** | [**List&lt;Condition&gt;**](Condition.md) | Conditions the trial refers to |  [optional] |
|**discrepancies** | **Object** | Discrepancies in trial&#39;s details between different sources |  [optional] |
|**documents** | [**List&lt;DocumentSummary&gt;**](DocumentSummary.md) | Documents related to the trial |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | Gender of the subjects of the trial |  [optional] |
|**hasPublishedResults** | **Boolean** | Trial has its results published (true/false) |  [optional] |
|**id** | **String** | ID of the trial |  |
|**identifiers** | **Object** | Object that maps the trial&#39;s sources ids with its identifiers. |  [optional] |
|**interventions** | [**List&lt;Intervention&gt;**](Intervention.md) | Interventions related to the trial |  |
|**locations** | [**List&lt;TrialLocation&gt;**](TrialLocation.md) | Locations related to the trial |  |
|**organisations** | [**List&lt;TrialOrganisation&gt;**](TrialOrganisation.md) | Organisations related to the trial |  |
|**persons** | [**List&lt;TrialPerson&gt;**](TrialPerson.md) | People related to the trial |  |
|**publicTitle** | **String** | Title of the trial |  |
|**publications** | [**List&lt;PublicationSummary&gt;**](PublicationSummary.md) | Publications referring the trial |  |
|**records** | [**List&lt;RecordSummary&gt;**](RecordSummary.md) | (published) records of the trial |  |
|**recruitmentStatus** | [**RecruitmentStatusEnum**](#RecruitmentStatusEnum) | Recruitment status of the trial |  [optional] |
|**registrationDate** | **OffsetDateTime** | Date the trial was registered |  [optional] |
|**resultsExemptionDate** | **OffsetDateTime** | Date when a certification of exemption has been filed for the trial |  [optional] |
|**risksOfBias** | [**List&lt;RiskOfBias&gt;**](RiskOfBias.md) |  |  |
|**sourceId** | **String** | ID of the trial&#39;s source |  [optional] |
|**sources** | **Object** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Completion status of the trial |  [optional] |
|**studyPhase** | **List&lt;String&gt;** | Phases of the study (e.g. &#x60;[\&quot;Phase 2\&quot;]&#x60; or &#x60;[\&quot;Phase 1\&quot;, \&quot;Phase 2\&quot;]&#x60;) |  [optional] |
|**targetSampleSize** | **Integer** | Target sample size for the trial |  [optional] |
|**url** | **String** | Source URL (where the trial was collected from) |  |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| BOTH | &quot;both&quot; |
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |



## Enum: RecruitmentStatusEnum

| Name | Value |
|---- | -----|
| RECRUITING | &quot;recruiting&quot; |
| NOT_RECRUITING | &quot;not_recruiting&quot; |
| UNKNOWN | &quot;unknown&quot; |
| OTHER | &quot;other&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ONGOING | &quot;ongoing&quot; |
| WITHDRAWN | &quot;withdrawn&quot; |
| SUSPENDED | &quot;suspended&quot; |
| TERMINATED | &quot;terminated&quot; |
| COMPLETE | &quot;complete&quot; |
| UNKNOWN | &quot;unknown&quot; |
| OTHER | &quot;other&quot; |



