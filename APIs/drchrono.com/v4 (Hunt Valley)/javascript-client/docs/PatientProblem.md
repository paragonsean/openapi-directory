# OpenapiJsClient.PatientProblem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateChanged** | **String** |  | [optional] 
**dateDiagnosis** | **String** |  | [optional] 
**dateOnset** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**doctor** | **Number** |  | 
**icdCode** | **String** | ICD9 or ICD10 code for the problem | [optional] 
**icdVersion** | **String** | Either &#x60;9&#x60; or &#x60;10&#x60;. If omitted in writing, default to 10. | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**infoUrl** | **String** | External URL with more information about the problem, intended for patient education | [optional] [readonly] 
**name** | **String** | Name of the problem | [optional] 
**notes** | **String** | Any additional notes by the provider | [optional] 
**patient** | **Number** |  | 
**snomedCtCode** | **String** | SnoMED code for the problem | [optional] 
**status** | **String** | Either &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;resolved&#x60;. If omitted in writing, default to &#x60;active&#x60; | [optional] 



## Enum: IcdVersionEnum


* `9` (value: `"9"`)

* `10` (value: `"10"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `resolved` (value: `"resolved"`)




