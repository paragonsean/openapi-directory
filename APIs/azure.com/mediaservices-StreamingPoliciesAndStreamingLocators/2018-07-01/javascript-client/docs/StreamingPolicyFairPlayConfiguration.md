# AzureMediaServices.StreamingPolicyFairPlayConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowPersistentLicense** | **Boolean** | All license to be persistent or not | 
**customLicenseAcquisitionUrlTemplate** | **String** | Template for the URL of the custom service delivering licenses to end user players.  Not required when using Azure Media Services for issuing licenses.  The template supports replaceable tokens that the service will update at runtime with the value specific to the request.  The currently supported token values are {AlternativeMediaId}, which is replaced with the value of StreamingLocatorId.AlternativeMediaId, and {ContentKeyId}, which is replaced with the value of identifier of the key being requested. | [optional] 


