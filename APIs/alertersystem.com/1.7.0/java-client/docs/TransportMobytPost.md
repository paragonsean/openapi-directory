

# TransportMobytPost

The TransportMobyt resource is a collection of transports that carry dispatched alerts to the external Mobyt service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**mobytAccessToken** | **String** | The access token for the Mobyt service. Stored in encrypted format. |  |
|**mobytFrom** | **String** | The sender for the Mobyt service. |  |
|**mobytTypeQuality** | **String** | The quality of your message: &#39;N&#39; for high, &#39;L&#39; for medium, &#39;LL&#39; for low, for the Mobyt service. |  |
|**mobytUserKey** | **String** | The user key for the Mobyt service. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



