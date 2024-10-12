

# GoogleCloudDiscoveryengineV1alphaDataStore

DataStore captures global settings and configs at the DataStore level.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aclEnabled** | **Boolean** | Immutable. Whether data in the DataStore has ACL information. If set to &#x60;true&#x60;, the source data must have ACL. ACL will be ingested when data is ingested by DocumentService.ImportDocuments methods. When ACL is enabled for the DataStore, Document can&#39;t be accessed by calling DocumentService.GetDocument or DocumentService.ListDocuments. Currently ACL is only supported in &#x60;GENERIC&#x60; industry vertical with non-&#x60;PUBLIC_WEBSITE&#x60; content config. |  [optional] |
|**contentConfig** | [**ContentConfigEnum**](#ContentConfigEnum) | Immutable. The content config of the data store. If this field is unset, the server behavior defaults to ContentConfig.NO_CONTENT. |  [optional] |
|**createTime** | **String** | Output only. Timestamp the DataStore was created at. |  [optional] [readonly] |
|**defaultSchemaId** | **String** | Output only. The id of the default Schema asscociated to this data store. |  [optional] [readonly] |
|**displayName** | **String** | Required. The data store display name. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |
|**documentProcessingConfig** | [**GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig**](GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig.md) |  |  [optional] |
|**idpConfig** | [**GoogleCloudDiscoveryengineV1alphaIdpConfig**](GoogleCloudDiscoveryengineV1alphaIdpConfig.md) |  |  [optional] |
|**industryVertical** | [**IndustryVerticalEnum**](#IndustryVerticalEnum) | Immutable. The industry vertical that the data store registers. |  [optional] |
|**name** | **String** | Immutable. The full resource name of the data store. Format: &#x60;projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}&#x60;. This field must be a UTF-8 encoded string with a length limit of 1024 characters. |  [optional] |
|**solutionTypes** | [**List&lt;SolutionTypesEnum&gt;**](#List&lt;SolutionTypesEnum&gt;) | The solutions that the data store enrolls. Available solutions for each industry_vertical: * &#x60;MEDIA&#x60;: &#x60;SOLUTION_TYPE_RECOMMENDATION&#x60; and &#x60;SOLUTION_TYPE_SEARCH&#x60;. * &#x60;SITE_SEARCH&#x60;: &#x60;SOLUTION_TYPE_SEARCH&#x60; is automatically enrolled. Other solutions cannot be enrolled. |  [optional] |
|**startingSchema** | [**GoogleCloudDiscoveryengineV1alphaSchema**](GoogleCloudDiscoveryengineV1alphaSchema.md) |  |  [optional] |



## Enum: ContentConfigEnum

| Name | Value |
|---- | -----|
| CONTENT_CONFIG_UNSPECIFIED | &quot;CONTENT_CONFIG_UNSPECIFIED&quot; |
| NO_CONTENT | &quot;NO_CONTENT&quot; |
| CONTENT_REQUIRED | &quot;CONTENT_REQUIRED&quot; |
| PUBLIC_WEBSITE | &quot;PUBLIC_WEBSITE&quot; |



## Enum: IndustryVerticalEnum

| Name | Value |
|---- | -----|
| INDUSTRY_VERTICAL_UNSPECIFIED | &quot;INDUSTRY_VERTICAL_UNSPECIFIED&quot; |
| GENERIC | &quot;GENERIC&quot; |
| MEDIA | &quot;MEDIA&quot; |



## Enum: List&lt;SolutionTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SOLUTION_TYPE_UNSPECIFIED&quot; |
| RECOMMENDATION | &quot;SOLUTION_TYPE_RECOMMENDATION&quot; |
| SEARCH | &quot;SOLUTION_TYPE_SEARCH&quot; |
| CHAT | &quot;SOLUTION_TYPE_CHAT&quot; |



