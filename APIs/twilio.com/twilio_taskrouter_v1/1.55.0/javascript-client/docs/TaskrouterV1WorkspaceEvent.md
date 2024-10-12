# TwilioTaskrouter.TaskrouterV1WorkspaceEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Event resource. | [optional] 
**actorSid** | **String** | The SID of the resource that triggered the event. | [optional] 
**actorType** | **String** | The type of resource that triggered the event. | [optional] 
**actorUrl** | **String** | The absolute URL of the resource that triggered the event. | [optional] 
**description** | **String** | A description of the event. | [optional] 
**eventData** | **Object** | Data about the event. For more information, see [Event types](https://www.twilio.com/docs/taskrouter/api/event#event-types). | [optional] 
**eventDate** | **Date** | The time the event was sent, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**eventDateMs** | **Number** | The time the event was sent in milliseconds. | [optional] 
**eventType** | **String** | The identifier for the event. | [optional] 
**resourceSid** | **String** | The SID of the object the event is most relevant to, such as a TaskSid, ReservationSid, or a  WorkerSid. | [optional] 
**resourceType** | **String** | The type of object the event is most relevant to, such as a Task, Reservation, or a Worker). | [optional] 
**resourceUrl** | **String** | The URL of the resource the event is most relevant to. | [optional] 
**sid** | **String** | The unique string that we created to identify the Event resource. | [optional] 
**source** | **String** | Where the Event originated. | [optional] 
**sourceIpAddress** | **String** | The IP from which the Event originated. | [optional] 
**url** | **String** | The absolute URL of the Event resource. | [optional] 
**workspaceSid** | **String** | The SID of the Workspace that contains the Event. | [optional] 


