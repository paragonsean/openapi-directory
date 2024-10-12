# AgcoApi.GlobalResourcesSharedModelsTranslationSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[GlobalResourcesSharedModelsTranslationSetAttribute]**](GlobalResourcesSharedModelsTranslationSetAttribute.md) | Attributes of the Translation Set | [optional] 
**fileIDs** | **[String]** | IDs for files related to this translation set. For example, the original and processed files | 
**id** | **Number** | The id of the TranslationSet. | [optional] 
**inDate** | **Date** | Read Only. The date the translation set was returned. | [optional] 
**notes** | **String** | Notes on the TranslationSet | [optional] 
**outDate** | **Date** | Read Only. The date the translation set was sent out. | [optional] 
**state** | **String** | An enum indicating the state of the translation set | 
**translationRequestID** | **Number** | Read Only. The Id of the TranslationRequest which generated this translation set. | [optional] 



## Enum: StateEnum


* `OutForProcessing` (value: `"OutForProcessing"`)

* `Processing` (value: `"Processing"`)

* `PendingApproval` (value: `"PendingApproval"`)

* `OutForTranslation` (value: `"OutForTranslation"`)

* `Cancelled` (value: `"Cancelled"`)

* `Completed` (value: `"Completed"`)




