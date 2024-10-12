# TwilioMonitor.MonitorV1Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Event resource. | [optional] 
**actorSid** | **String** | The SID of the actor that caused the event, if available. Can be &#x60;null&#x60;. | [optional] 
**actorType** | **String** | The type of actor that caused the event. Can be: &#x60;user&#x60; for a change made by a logged-in user in the Twilio Console, &#x60;account&#x60; for an event caused by an API request by an authenticating Account, &#x60;twilio-admin&#x60; for an event caused by a Twilio employee, and so on. | [optional] 
**description** | **String** | A description of the event. Can be &#x60;null&#x60;. | [optional] 
**eventData** | **Object** | An object with additional data about the event. The  contents depend on &#x60;event_type&#x60;. For example, event-types of the form &#x60;RESOURCE.updated&#x60;, this value contains a &#x60;resource_properties&#x60; dictionary that describes the previous and updated properties of the resource. | [optional] 
**eventDate** | **Date** | The date and time in GMT when the event was recorded specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**eventType** | **String** | The event&#39;s type. Event-types are typically in the form: &#x60;RESOURCE_TYPE.ACTION&#x60;, where &#x60;RESOURCE_TYPE&#x60; is the type of resource that was affected and &#x60;ACTION&#x60; is what happened to it. For example, &#x60;phone-number.created&#x60;. For a full list of all event-types, see the [Monitor Event Types](https://www.twilio.com/docs/usage/monitor-events#event-types). | [optional] 
**links** | **Object** | The absolute URLs of related resources. | [optional] 
**resourceSid** | **String** | The SID of the resource that was affected. | [optional] 
**resourceType** | **String** | The type of resource that was affected. For a full list of all resource-types, see the [Monitor Event Types](https://www.twilio.com/docs/usage/monitor-events#event-types). | [optional] 
**sid** | **String** | The unique string that we created to identify the Event resource. | [optional] 
**source** | **String** | The originating system or interface that caused the event.  Can be: &#x60;web&#x60; for events caused by user action in the Twilio Console, &#x60;api&#x60; for events caused by a request to our API, or   &#x60;twilio&#x60; for events caused by an automated or internal Twilio system. | [optional] 
**sourceIpAddress** | **String** | The IP address of the source, if the source is outside the Twilio cloud. This value is &#x60;null&#x60; for events with &#x60;source&#x60; of &#x60;twilio&#x60; | [optional] 
**url** | **String** | The absolute URL of the resource that was affected. Can be &#x60;null&#x60;. | [optional] 


