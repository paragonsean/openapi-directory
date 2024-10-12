# DialogflowApi.GoogleCloudDialogflowV2Fulfillment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Optional. The human-readable name of the fulfillment, unique within the agent. This field is not used for Fulfillment in an Environment. | [optional] 
**enabled** | **Boolean** | Optional. Whether fulfillment is enabled. | [optional] 
**features** | [**[GoogleCloudDialogflowV2FulfillmentFeature]**](GoogleCloudDialogflowV2FulfillmentFeature.md) | Optional. The field defines whether the fulfillment is enabled for certain features. | [optional] 
**genericWebService** | [**GoogleCloudDialogflowV2FulfillmentGenericWebService**](GoogleCloudDialogflowV2FulfillmentGenericWebService.md) |  | [optional] 
**name** | **String** | Required. The unique identifier of the fulfillment. Supported formats: - &#x60;projects//agent/fulfillment&#x60; - &#x60;projects//locations//agent/fulfillment&#x60; This field is not used for Fulfillment in an Environment. | [optional] 


