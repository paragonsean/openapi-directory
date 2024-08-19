# FirebaseMlApi.Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeOperations** | [**[Operation]**](Operation.md) | Output only. Lists operation ids associated with this model whose status is NOT done. | [optional] [readonly] 
**createTime** | **String** | Output only. Timestamp when this model was created in Firebase ML. | [optional] [readonly] 
**displayName** | **String** | Required. The name of the model to create. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores(_) and ASCII digits 0-9. It must start with a letter. | [optional] 
**etag** | **String** | Output only. See RFC7232 https://tools.ietf.org/html/rfc7232#section-2.3 | [optional] [readonly] 
**modelHash** | **String** | Output only. The model_hash will change if a new file is available for download. | [optional] [readonly] 
**name** | **String** | The resource name of the Model. Model names have the form &#x60;projects/{project_id}/models/{model_id}&#x60; The name is ignored when creating a model. | [optional] 
**state** | [**ModelState**](ModelState.md) |  | [optional] 
**tags** | **[String]** | User defined tags which can be used to group/filter models during listing | [optional] 
**tfliteModel** | [**TfLiteModel**](TfLiteModel.md) |  | [optional] 
**updateTime** | **String** | Output only. Timestamp when this model was updated in Firebase ML. | [optional] [readonly] 


