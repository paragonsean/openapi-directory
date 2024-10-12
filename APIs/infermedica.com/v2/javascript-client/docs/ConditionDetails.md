# InfermedicaApi.ConditionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acuteness** | **String** |  | [optional] 
**categories** | **[String]** |  | 
**commonName** | **String** |  | [optional] 
**extras** | **{String: Object}** | additional content, like custom properties or images | [optional] 
**id** | **String** |  | 
**name** | **String** |  | 
**prevalence** | **String** |  | [optional] 
**severity** | **String** |  | [optional] 
**sexFilter** | **String** |  | 
**triageLevel** | **String** |  | [optional] 



## Enum: AcutenessEnum


* `chronic` (value: `"chronic"`)

* `chronic_with_exacerbations` (value: `"chronic_with_exacerbations"`)

* `acute_potentially_chronic` (value: `"acute_potentially_chronic"`)

* `acute` (value: `"acute"`)





## Enum: PrevalenceEnum


* `very_rare` (value: `"very_rare"`)

* `rare` (value: `"rare"`)

* `moderate` (value: `"moderate"`)

* `common` (value: `"common"`)





## Enum: SeverityEnum


* `mild` (value: `"mild"`)

* `moderate` (value: `"moderate"`)

* `severe` (value: `"severe"`)





## Enum: SexFilterEnum


* `both` (value: `"both"`)

* `male` (value: `"male"`)

* `female` (value: `"female"`)





## Enum: TriageLevelEnum


* `emergency_ambulance` (value: `"emergency_ambulance"`)

* `emergency` (value: `"emergency"`)

* `consultation_24` (value: `"consultation_24"`)

* `consultation` (value: `"consultation"`)

* `self_care` (value: `"self_care"`)




