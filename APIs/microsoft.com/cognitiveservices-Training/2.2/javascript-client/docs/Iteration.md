# CustomVisionTrainingClient.Iteration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classificationType** | **String** | Gets the classification type of the project. | [optional] [readonly] 
**created** | **Date** | Gets the time this iteration was completed. | [optional] [readonly] 
**domainId** | **String** | Get or sets a guid of the domain the iteration has been trained on. | [optional] [readonly] 
**exportable** | **Boolean** | Whether the iteration can be exported to another format for download. | [optional] [readonly] 
**id** | **String** | Gets the id of the iteration. | [optional] [readonly] 
**isDefault** | **Boolean** | Gets or sets a value indicating whether the iteration is the default iteration for the project. | [optional] 
**lastModified** | **Date** | Gets the time this iteration was last modified. | [optional] [readonly] 
**name** | **String** | Gets or sets the name of the iteration. | [optional] 
**projectId** | **String** | Gets The project id. of the iteration. | [optional] [readonly] 
**status** | **String** | Gets the current iteration status. | [optional] [readonly] 
**trainedAt** | **Date** | Gets the time this iteration was last modified. | [optional] [readonly] 



## Enum: ClassificationTypeEnum


* `Multiclass` (value: `"Multiclass"`)

* `Multilabel` (value: `"Multilabel"`)




