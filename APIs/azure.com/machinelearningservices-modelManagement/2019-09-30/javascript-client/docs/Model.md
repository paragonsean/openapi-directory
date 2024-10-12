# AzureMachineLearningModelManagementService.Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTime** | **Date** | The Model creation time (UTC). | [optional] [readonly] 
**datasets** | [**[DatasetReference]**](DatasetReference.md) | The list of datasets associated with the model. | [optional] 
**description** | **String** | The Model description text. | [optional] 
**experimentName** | **String** | The name of the experiment where this model was created. | [optional] 
**framework** | **String** | The Model framework. | [optional] 
**frameworkVersion** | **String** | The Model framework version. | [optional] 
**id** | **String** | The Model Id. | [optional] 
**kvTags** | **{String: String}** | The Model tag dictionary. Items are mutable. | [optional] 
**mimeType** | **String** | The MIME type of Model content. For more details about MIME type, please open https://www.iana.org/assignments/media-types/media-types.xhtml | 
**modifiedTime** | **Date** | The Model last modified time (UTC). | [optional] [readonly] 
**name** | **String** | The Model name. | 
**parentModelId** | **String** | The Parent Model Id. | [optional] 
**properties** | **{String: String}** | The Model property dictionary. Properties are immutable. | [optional] 
**runId** | **String** | The RunId that created this model. | [optional] 
**unpack** | **Boolean** | Indicates whether we need to unpack the Model during docker Image creation. | [optional] 
**url** | **String** | The URL of the Model. Usually a SAS URL. | 
**version** | **Number** | The Model version assigned by Model Management Service. | [optional] 


