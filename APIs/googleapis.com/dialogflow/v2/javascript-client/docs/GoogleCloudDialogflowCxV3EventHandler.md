# DialogflowApi.GoogleCloudDialogflowCxV3EventHandler

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **String** | Required. The name of the event to handle. | [optional] 
**name** | **String** | Output only. The unique identifier of this event handler. | [optional] [readonly] 
**targetFlow** | **String** | The target flow to transition to. Format: &#x60;projects//locations//agents//flows/&#x60;. | [optional] 
**targetPage** | **String** | The target page to transition to. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. | [optional] 
**triggerFulfillment** | [**GoogleCloudDialogflowCxV3Fulfillment**](GoogleCloudDialogflowCxV3Fulfillment.md) |  | [optional] 


