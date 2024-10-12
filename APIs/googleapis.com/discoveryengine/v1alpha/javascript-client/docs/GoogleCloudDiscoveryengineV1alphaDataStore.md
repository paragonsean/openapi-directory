# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaDataStore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aclEnabled** | **Boolean** | Immutable. Whether data in the DataStore has ACL information. If set to &#x60;true&#x60;, the source data must have ACL. ACL will be ingested when data is ingested by DocumentService.ImportDocuments methods. When ACL is enabled for the DataStore, Document can&#39;t be accessed by calling DocumentService.GetDocument or DocumentService.ListDocuments. Currently ACL is only supported in &#x60;GENERIC&#x60; industry vertical with non-&#x60;PUBLIC_WEBSITE&#x60; content config. | [optional] 
**contentConfig** | **String** | Immutable. The content config of the data store. If this field is unset, the server behavior defaults to ContentConfig.NO_CONTENT. | [optional] 
**createTime** | **String** | Output only. Timestamp the DataStore was created at. | [optional] [readonly] 
**defaultSchemaId** | **String** | Output only. The id of the default Schema asscociated to this data store. | [optional] [readonly] 
**displayName** | **String** | Required. The data store display name. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. | [optional] 
**documentProcessingConfig** | [**GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig**](GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig.md) |  | [optional] 
**idpConfig** | [**GoogleCloudDiscoveryengineV1alphaIdpConfig**](GoogleCloudDiscoveryengineV1alphaIdpConfig.md) |  | [optional] 
**industryVertical** | **String** | Immutable. The industry vertical that the data store registers. | [optional] 
**name** | **String** | Immutable. The full resource name of the data store. Format: &#x60;projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}&#x60;. This field must be a UTF-8 encoded string with a length limit of 1024 characters. | [optional] 
**solutionTypes** | **[String]** | The solutions that the data store enrolls. Available solutions for each industry_vertical: * &#x60;MEDIA&#x60;: &#x60;SOLUTION_TYPE_RECOMMENDATION&#x60; and &#x60;SOLUTION_TYPE_SEARCH&#x60;. * &#x60;SITE_SEARCH&#x60;: &#x60;SOLUTION_TYPE_SEARCH&#x60; is automatically enrolled. Other solutions cannot be enrolled. | [optional] 
**startingSchema** | [**GoogleCloudDiscoveryengineV1alphaSchema**](GoogleCloudDiscoveryengineV1alphaSchema.md) |  | [optional] 



## Enum: ContentConfigEnum


* `CONTENT_CONFIG_UNSPECIFIED` (value: `"CONTENT_CONFIG_UNSPECIFIED"`)

* `NO_CONTENT` (value: `"NO_CONTENT"`)

* `CONTENT_REQUIRED` (value: `"CONTENT_REQUIRED"`)

* `PUBLIC_WEBSITE` (value: `"PUBLIC_WEBSITE"`)





## Enum: IndustryVerticalEnum


* `INDUSTRY_VERTICAL_UNSPECIFIED` (value: `"INDUSTRY_VERTICAL_UNSPECIFIED"`)

* `GENERIC` (value: `"GENERIC"`)

* `MEDIA` (value: `"MEDIA"`)





## Enum: [SolutionTypesEnum]


* `UNSPECIFIED` (value: `"SOLUTION_TYPE_UNSPECIFIED"`)

* `RECOMMENDATION` (value: `"SOLUTION_TYPE_RECOMMENDATION"`)

* `SEARCH` (value: `"SOLUTION_TYPE_SEARCH"`)

* `CHAT` (value: `"SOLUTION_TYPE_CHAT"`)




