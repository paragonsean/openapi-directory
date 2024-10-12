# AlerterSystemApi.TransportTelnyxPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**telnyxApiKey** | **String** | The API key for the Telnyx service. Stored in encrypted format. | 
**telnyxFrom** | **String** | The from value for the Telnyx service. | 
**telnyxMessagingProfileId** | **String** | The messaging profile ID (You need this in order to show a name to the recipient instead of just the phone number) for the Telnyx service. | 
**transportName** | **String** | The name of the transport. | 


