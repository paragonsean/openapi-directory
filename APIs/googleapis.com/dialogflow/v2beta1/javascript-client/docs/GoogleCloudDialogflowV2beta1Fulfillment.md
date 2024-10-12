# DialogflowApi.GoogleCloudDialogflowV2beta1Fulfillment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The human-readable name of the fulfillment, unique within the agent. This field is not used for Fulfillment in an Environment. | [optional] 
**enabled** | **Boolean** | Whether fulfillment is enabled. | [optional] 
**features** | [**[GoogleCloudDialogflowV2beta1FulfillmentFeature]**](GoogleCloudDialogflowV2beta1FulfillmentFeature.md) | The field defines whether the fulfillment is enabled for certain features. | [optional] 
**genericWebService** | [**GoogleCloudDialogflowV2beta1FulfillmentGenericWebService**](GoogleCloudDialogflowV2beta1FulfillmentGenericWebService.md) |  | [optional] 
**name** | **String** | Required. The unique identifier of the fulfillment. Supported formats: - &#x60;projects//agent/fulfillment&#x60; - &#x60;projects//locations//agent/fulfillment&#x60; This field is not used for Fulfillment in an Environment. | [optional] 


