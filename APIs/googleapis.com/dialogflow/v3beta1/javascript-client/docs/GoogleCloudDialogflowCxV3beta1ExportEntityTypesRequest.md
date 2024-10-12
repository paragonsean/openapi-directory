# DialogflowApi.GoogleCloudDialogflowCxV3beta1ExportEntityTypesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataFormat** | **String** | Optional. The data format of the exported entity types. If not specified, &#x60;BLOB&#x60; is assumed. | [optional] 
**entityTypes** | **[String]** | Required. The name of the entity types to export. Format: &#x60;projects//locations//agents//entityTypes/&#x60;. | [optional] 
**entityTypesContentInline** | **Boolean** | Optional. The option to return the serialized entity types inline. | [optional] 
**entityTypesUri** | **String** | Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the entity types to. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a write operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). | [optional] 
**languageCode** | **String** | Optional. The language to retrieve the entity type for. The following fields are language dependent: * &#x60;EntityType.entities.value&#x60; * &#x60;EntityType.entities.synonyms&#x60; * &#x60;EntityType.excluded_phrases.value&#x60; If not specified, all language dependent fields will be retrieved. [Many languages](https://cloud.google.com/dialogflow/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 



## Enum: DataFormatEnum


* `DATA_FORMAT_UNSPECIFIED` (value: `"DATA_FORMAT_UNSPECIFIED"`)

* `BLOB` (value: `"BLOB"`)

* `JSON_PACKAGE` (value: `"JSON_PACKAGE"`)




