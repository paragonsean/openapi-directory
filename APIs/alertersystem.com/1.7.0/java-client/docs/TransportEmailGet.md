

# TransportEmailGet

The TransportEmail resource is a collection of transports that carry dispatched alerts to external SMTP email services.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**emailFromAddress** | **String** | The sender email address for the SMTP Email service. |  |
|**emailFromName** | **String** | The sender name for the SMTP Email service. |  |
|**emailPassword** | **String** | The password for the SMTP Email service. Stored in encrypted format. |  |
|**emailPort** | **Integer** | The port for the SMTP Email service. |  |
|**emailServer** | **String** | The server for the SMTP Email service. |  |
|**emailUsername** | **String** | The username for the SMTP Email service. |  |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



