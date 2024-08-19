# GitHubV3RestApi.HookDeliveryItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The type of activity for the event that triggered the delivery. | 
**deliveredAt** | **Date** | Time when the webhook delivery occurred. | 
**duration** | **Number** | Time spent delivering. | 
**event** | **String** | The event that triggered the delivery. | 
**guid** | **String** | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). | 
**id** | **Number** | Unique identifier of the webhook delivery. | 
**installationId** | **Number** | The id of the GitHub App installation associated with this event. | 
**redelivery** | **Boolean** | Whether the webhook delivery is a redelivery. | 
**repositoryId** | **Number** | The id of the repository associated with this event. | 
**status** | **String** | Describes the response returned after attempting the delivery. | 
**statusCode** | **Number** | Status code received when delivery was made. | 


