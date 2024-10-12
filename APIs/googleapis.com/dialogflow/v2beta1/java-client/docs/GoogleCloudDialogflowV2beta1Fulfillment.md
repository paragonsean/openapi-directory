

# GoogleCloudDialogflowV2beta1Fulfillment

By default, your agent responds to a matched intent with a static response. As an alternative, you can provide a more dynamic response by using fulfillment. When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define. For example, if an end-user wants to schedule a haircut on Friday, your service can check your database and respond to the end-user with availability information for Friday. For more information, see the [fulfillment guide](https://cloud.google.com/dialogflow/docs/fulfillment-overview).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The human-readable name of the fulfillment, unique within the agent. This field is not used for Fulfillment in an Environment. |  [optional] |
|**enabled** | **Boolean** | Whether fulfillment is enabled. |  [optional] |
|**features** | [**List&lt;GoogleCloudDialogflowV2beta1FulfillmentFeature&gt;**](GoogleCloudDialogflowV2beta1FulfillmentFeature.md) | The field defines whether the fulfillment is enabled for certain features. |  [optional] |
|**genericWebService** | [**GoogleCloudDialogflowV2beta1FulfillmentGenericWebService**](GoogleCloudDialogflowV2beta1FulfillmentGenericWebService.md) |  |  [optional] |
|**name** | **String** | Required. The unique identifier of the fulfillment. Supported formats: - &#x60;projects//agent/fulfillment&#x60; - &#x60;projects//locations//agent/fulfillment&#x60; This field is not used for Fulfillment in an Environment. |  [optional] |



