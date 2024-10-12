# BooksApi.Annotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterSelectedText** | **String** | Anchor text after excerpt. For requests, if the user bookmarked a screen that has no flowing text on it, then this field should be empty. | [optional] 
**beforeSelectedText** | **String** | Anchor text before excerpt. For requests, if the user bookmarked a screen that has no flowing text on it, then this field should be empty. | [optional] 
**clientVersionRanges** | [**AnnotationClientVersionRanges**](AnnotationClientVersionRanges.md) |  | [optional] 
**created** | **String** | Timestamp for the created time of this annotation. | [optional] 
**currentVersionRanges** | [**AnnotationCurrentVersionRanges**](AnnotationCurrentVersionRanges.md) |  | [optional] 
**data** | **String** | User-created data for this annotation. | [optional] 
**deleted** | **Boolean** | Indicates that this annotation is deleted. | [optional] 
**highlightStyle** | **String** | The highlight style for this annotation. | [optional] 
**id** | **String** | Id of this annotation, in the form of a GUID. | [optional] 
**kind** | **String** | Resource type. | [optional] 
**layerId** | **String** | The layer this annotation is for. | [optional] 
**layerSummary** | [**AnnotationLayerSummary**](AnnotationLayerSummary.md) |  | [optional] 
**pageIds** | **[String]** | Pages that this annotation spans. | [optional] 
**selectedText** | **String** | Excerpt from the volume. | [optional] 
**selfLink** | **String** | URL to this resource. | [optional] 
**updated** | **String** | Timestamp for the last time this annotation was modified. | [optional] 
**volumeId** | **String** | The volume that this annotation belongs to. | [optional] 


