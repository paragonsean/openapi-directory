# InfermedicaApi.SymptomDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** |  | [optional] 
**children** | **Object** | list of child symptoms | [optional] 
**commonName** | **String** |  | [optional] 
**extras** | **{String: Object}** | additional content, like custom properties or images | [optional] 
**id** | **String** |  | 
**imageSource** | **String** |  | [optional] 
**imageUrl** | **String** |  | [optional] 
**name** | **String** |  | 
**parentId** | **String** | id of parent symptom | [optional] 
**parentRelation** | **String** | type of relation with parent symptom | [optional] 
**question** | **String** | only available in object details, not in listing | 
**sexFilter** | **String** |  | 



## Enum: ParentRelationEnum


* `base` (value: `"base"`)

* `duration` (value: `"duration"`)

* `severity` (value: `"severity"`)

* `character` (value: `"character"`)

* `exacerbating_factor` (value: `"exacerbating_factor"`)

* `diminishing_factor` (value: `"diminishing_factor"`)

* `location` (value: `"location"`)

* `radiation` (value: `"radiation"`)





## Enum: SexFilterEnum


* `both` (value: `"both"`)

* `male` (value: `"male"`)

* `female` (value: `"female"`)




