# AlerterSystemApi.TransportTwilioGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 
**twilioFrom** | **String** | The sender for the Twilio service. | 
**twilioSid** | **String** | The SID for the Twilio service. | 
**twilioToken** | **String** | The token for the Twilio service. Stored in encrypted format. | 


