# AzureMediaServices.EnvelopeEncryption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clearTracks** | [**[TrackSelection]**](TrackSelection.md) | Representing which tracks should not be encrypted | [optional] 
**contentKeys** | [**StreamingPolicyContentKeys**](StreamingPolicyContentKeys.md) |  | [optional] 
**customKeyAcquisitionUrlTemplate** | **String** | Template for the URL of the custom service delivering keys to end user players.  Not required when using Azure Media Services for issuing keys.  The template supports replaceable tokens that the service will update at runtime with the value specific to the request.  The currently supported token values are {AlternativeMediaId}, which is replaced with the value of StreamingLocatorId.AlternativeMediaId, and {ContentKeyId}, which is replaced with the value of identifier of the key being requested. | [optional] 
**enabledProtocols** | [**EnabledProtocols**](EnabledProtocols.md) |  | [optional] 


