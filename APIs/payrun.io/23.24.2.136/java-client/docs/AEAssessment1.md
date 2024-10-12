

# AEAssessment1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**age** | **Integer** | The a e assessments&#39; age |  [optional] |
|**assessmentCode** | [**AssessmentCodeEnum**](#AssessmentCodeEnum) | The a e assessments&#39; assessment code |  [optional] |
|**assessmentDate** | **LocalDate** | The a e assessments&#39; assessment date |  [optional] |
|**assessmentEvent** | [**AssessmentEventEnum**](#AssessmentEventEnum) | The a e assessments&#39; assessment event |  [optional] |
|**assessmentOverride** | [**AssessmentOverrideEnum**](#AssessmentOverrideEnum) | The a e assessments&#39; assessment override |  [optional] |
|**assessmentResult** | [**AssessmentResultEnum**](#AssessmentResultEnum) | The a e assessments&#39; assessment result |  [optional] |
|**isMemberOfAlternativePensionScheme** | **Boolean** | The a e assessments&#39; is member of alternative pension scheme |  [optional] |
|**optOutWindowEndDate** | **LocalDate** | The a e assessments&#39; opt out window end date |  [optional] |
|**qualifyingEarnings** | **Double** | The a e assessments&#39; qualifying earnings |  [optional] |
|**reenrolmentDate** | **LocalDate** | The a e assessments&#39; reenrolment date |  [optional] |
|**statePensionAge** | **Integer** | The a e assessments&#39; state pension age |  [optional] |
|**statePensionDate** | **LocalDate** | The a e assessments&#39; state pension date |  [optional] |
|**taxPeriod** | **Integer** | The a e assessments&#39; tax period |  [optional] |
|**taxYear** | **Integer** | The a e assessments&#39; tax year |  [optional] |



## Enum: AssessmentCodeEnum

| Name | Value |
|---- | -----|
| EXCLUDED | &quot;Excluded&quot; |
| ELIGIBLE_JOB_HOLDER | &quot;EligibleJobHolder&quot; |
| NON_ELIGIBLE_JOB_HOLDER | &quot;NonEligibleJobHolder&quot; |
| ENTITLED_WORKER | &quot;EntitledWorker&quot; |



## Enum: AssessmentEventEnum

| Name | Value |
|---- | -----|
| NON_ENROLMENT_EVENT | &quot;NonEnrolmentEvent&quot; |
| AUTOMATIC_ENROLMENT | &quot;AutomaticEnrolment&quot; |
| OPT_IN | &quot;OptIn&quot; |
| VOLUNTARY_JOINER | &quot;VoluntaryJoiner&quot; |
| CONTRACTUAL_ENROLMENT | &quot;ContractualEnrolment&quot; |



## Enum: AssessmentOverrideEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| OPT_OUT | &quot;OptOut&quot; |
| OPT_IN | &quot;OptIn&quot; |
| VOLUNTARY_JOINER | &quot;VoluntaryJoiner&quot; |
| CONTRACTUAL_PENSION | &quot;ContractualPension&quot; |
| CEASED_MEMBERSHIP | &quot;CeasedMembership&quot; |
| LEAVER | &quot;Leaver&quot; |
| EXCLUDED | &quot;Excluded&quot; |



## Enum: AssessmentResultEnum

| Name | Value |
|---- | -----|
| INCONCLUSIVE | &quot;Inconclusive&quot; |
| NO_CHANGE | &quot;NoChange&quot; |
| ENROL | &quot;Enrol&quot; |
| EXIT | &quot;Exit&quot; |



