

# TemplateMetadata

Metadata describing a template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. A description of the template. |  [optional] |
|**name** | **String** | Required. The name of the template. |  [optional] |
|**parameters** | [**List&lt;ParameterMetadata&gt;**](ParameterMetadata.md) | The parameters for the template. |  [optional] |
|**streaming** | **Boolean** | Optional. Indicates if the template is streaming or not. |  [optional] |
|**supportsAtLeastOnce** | **Boolean** | Optional. Indicates if the streaming template supports at least once mode. |  [optional] |
|**supportsExactlyOnce** | **Boolean** | Optional. Indicates if the streaming template supports exactly once mode. |  [optional] |



