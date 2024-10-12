

# TransportEmailPost

The TransportEmail resource is a collection of transports that carry dispatched alerts to external SMTP email services.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**emailFromAddress** | **String** | The sender email address for the SMTP Email service. |  |
|**emailFromName** | **String** | The sender name for the SMTP Email service. |  |
|**emailPassword** | **String** | The password for the SMTP Email service. Stored in encrypted format. |  |
|**emailPort** | **Integer** | The port for the SMTP Email service. |  |
|**emailServer** | **String** | The server for the SMTP Email service. |  |
|**emailUsername** | **String** | The username for the SMTP Email service. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



