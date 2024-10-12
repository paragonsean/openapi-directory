# GitHubV3RestApi.HookDelivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The type of activity for the event that triggered the delivery. | 
**deliveredAt** | **Date** | Time when the delivery was delivered. | 
**duration** | **Number** | Time spent delivering. | 
**event** | **String** | The event that triggered the delivery. | 
**guid** | **String** | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). | 
**id** | **Number** | Unique identifier of the delivery. | 
**installationId** | **Number** | The id of the GitHub App installation associated with this event. | 
**redelivery** | **Boolean** | Whether the delivery is a redelivery. | 
**repositoryId** | **Number** | The id of the repository associated with this event. | 
**request** | [**HookDeliveryRequest**](HookDeliveryRequest.md) |  | 
**response** | [**HookDeliveryResponse**](HookDeliveryResponse.md) |  | 
**status** | **String** | Description of the status of the attempted delivery | 
**statusCode** | **Number** | Status code received when delivery was made. | 
**url** | **String** | The URL target of the delivery. | [optional] 


