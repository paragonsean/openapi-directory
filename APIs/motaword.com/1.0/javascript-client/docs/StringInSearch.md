# MotaWordApi.StringInSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileId** | **Number** |  | [optional] 
**internalProjectId** | **Number** |  | [optional] 
**lastUpdated** | **Date** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z | [optional] 
**projectId** | **Number** |  | [optional] 
**searchScore** | **Number** |  | [optional] 
**source** | **String** |  | [optional] 
**status** | [**StringTranslationState**](StringTranslationState.md) |  | [optional] 
**stringId** | **Number** |  | [optional] 
**target** | **String** |  | [optional] 
**targets** | **[String]** |  | [optional] 
**tmName** | **String** |  | [optional] 
**type** | **String** | String search result typ from ZNT. Options are LOCAL_PROJECT, IMPORTED_TM. Imported TM results should probably not be visible to end users. | [optional] 



## Enum: TypeEnum


* `LOCAL_PROJECT` (value: `"LOCAL_PROJECT"`)

* `IMPORTED_TM` (value: `"IMPORTED_TM"`)




