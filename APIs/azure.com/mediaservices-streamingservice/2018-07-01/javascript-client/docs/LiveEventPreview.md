# AzureMediaServices.LiveEventPreview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessControl** | [**LiveEventPreviewAccessControl**](LiveEventPreviewAccessControl.md) |  | [optional] 
**alternativeMediaId** | **String** | An Alternative Media Identifier associated with the StreamingLocator created for the preview.  This value is specified at creation time and cannot be updated.  The identifier can be used in the CustomLicenseAcquisitionUrlTemplate or the CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in the StreamingPolicyName field. | [optional] 
**endpoints** | [**[LiveEventEndpoint]**](LiveEventEndpoint.md) | The endpoints for preview. | [optional] 
**previewLocator** | **String** | The identifier of the preview locator in Guid format.  Specifying this at creation time allows the caller to know the preview locator url before the event is created.  If omitted, the service will generate a random identifier.  This value cannot be updated once the live event is created. | [optional] 
**streamingPolicyName** | **String** | The name of streaming policy used for the LiveEvent preview.  This value is specified at creation time and cannot be updated. | [optional] 


