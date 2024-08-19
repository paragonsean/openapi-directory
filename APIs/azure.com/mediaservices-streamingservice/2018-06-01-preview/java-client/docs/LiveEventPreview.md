

# LiveEventPreview

The Live Event preview.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessControl** | [**LiveEventPreviewAccessControl**](LiveEventPreviewAccessControl.md) |  |  [optional] |
|**alternativeMediaId** | **String** | An Alternative Media Identifier associated with the preview url.  This identifier can be used to distinguish the preview of different live events for authorization purposes in the CustomLicenseAcquisitionUrlTemplate or the CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in the StreamingPolicyName field. |  [optional] |
|**endpoints** | [**List&lt;LiveEventEndpoint&gt;**](LiveEventEndpoint.md) | The endpoints for preview. |  [optional] |
|**previewLocator** | **String** | The preview locator Guid. |  [optional] |
|**streamingPolicyName** | **String** | The name of streaming policy used for LiveEvent preview |  [optional] |



