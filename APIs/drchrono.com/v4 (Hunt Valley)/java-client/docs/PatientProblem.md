

# PatientProblem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateChanged** | **String** |  |  [optional] |
|**dateDiagnosis** | **String** |  |  [optional] |
|**dateOnset** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**doctor** | **Integer** |  |  |
|**icdCode** | **String** | ICD9 or ICD10 code for the problem |  [optional] |
|**icdVersion** | [**IcdVersionEnum**](#IcdVersionEnum) | Either &#x60;9&#x60; or &#x60;10&#x60;. If omitted in writing, default to 10. |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**infoUrl** | **String** | External URL with more information about the problem, intended for patient education |  [optional] [readonly] |
|**name** | **String** | Name of the problem |  [optional] |
|**notes** | **String** | Any additional notes by the provider |  [optional] |
|**patient** | **Integer** |  |  |
|**snomedCtCode** | **String** | SnoMED code for the problem |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Either &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;resolved&#x60;. If omitted in writing, default to &#x60;active&#x60; |  [optional] |



## Enum: IcdVersionEnum

| Name | Value |
|---- | -----|
| _9 | &quot;9&quot; |
| _10 | &quot;10&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| RESOLVED | &quot;resolved&quot; |



