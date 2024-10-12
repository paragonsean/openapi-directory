# InfermedicaApi.Evidence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choiceId** | **String** |  | 
**id** | **String** | id of observation or condition | 
**observedAt** | **String** | time when evidence was observed in ISO 8601 format | [optional] 
**source** | **String** | Flag describing evidence origin | [optional] 



## Enum: ChoiceIdEnum


* `present` (value: `"present"`)

* `absent` (value: `"absent"`)

* `unknown` (value: `"unknown"`)





## Enum: SourceEnum


* `initial` (value: `"initial"`)

* `suggest` (value: `"suggest"`)

* `predefined` (value: `"predefined"`)

* `red_flags` (value: `"red_flags"`)




