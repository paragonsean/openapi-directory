

# TransportZendeskJsonldPut

The TransportZendesk resource is a collection of transports that carry dispatched alerts to the external Zendesk service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |
|**zendeskEmail** | **String** | The login email address for the Zendesk service. |  |
|**zendeskHost** | **String** | The host name for the Zendesk service (domain.zendesk.com). |  |
|**zendeskToken** | **String** | The token for the Zendesk service. Stored in encrypted format. |  |



