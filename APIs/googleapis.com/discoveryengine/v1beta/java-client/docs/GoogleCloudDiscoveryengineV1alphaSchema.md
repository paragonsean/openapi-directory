

# GoogleCloudDiscoveryengineV1alphaSchema

Defines the structure and layout of a type of document data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldConfigs** | [**List&lt;GoogleCloudDiscoveryengineV1alphaFieldConfig&gt;**](GoogleCloudDiscoveryengineV1alphaFieldConfig.md) | Output only. Configurations for fields of the schema. |  [optional] [readonly] |
|**jsonSchema** | **String** | The JSON representation of the schema. |  [optional] |
|**name** | **String** | Immutable. The full resource name of the schema, in the format of &#x60;projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/schemas/{schema}&#x60;. This field must be a UTF-8 encoded string with a length limit of 1024 characters. |  [optional] |
|**structSchema** | **Map&lt;String, Object&gt;** | The structured representation of the schema. |  [optional] |



