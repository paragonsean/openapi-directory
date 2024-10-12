

# TransportMattermostPost

The TransportMattermost resource is a collection of transports that carry dispatched alerts to the external Mattermost service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**mattermostAccessToken** | **String** | The access token for the Mattermost service. Stored in encrypted format. |  |
|**mattermostChannel** | **String** | The default channel ID for the Mattermost service. |  |
|**mattermostHost** | **String** | The host for the Mattermost service. |  |
|**mattermostPath** | **String** | The optional path for the Mattermost service. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



