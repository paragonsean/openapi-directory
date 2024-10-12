

# TransportAlertaJsonldPut

The TransportAlerta resource is a collection of transports that carry dispatched alerts to the external Alerta service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertaApiKey** | **String** | The API key for the Alerta service. |  |
|**alertaCorrelate** | **String** | The comma-separated list of related event names for the Alerta service. |  [optional] |
|**alertaEnvironment** | **String** | The environment value for the Alerta service. |  [optional] |
|**alertaEvent** | **String** | The event value for the Alerta service. |  |
|**alertaGroup** | **String** | The group value for the Alerta service. |  [optional] |
|**alertaHost** | **String** | The host name for the Alerta service (omit the \&quot;https://\&quot; part). |  |
|**alertaOrigin** | **String** | The origin value for the Alerta service. |  [optional] |
|**alertaResource** | **String** | The resource value for the Alerta service. |  |
|**alertaService** | **String** | The comma-separated list of affected services for the Alerta service. |  [optional] |
|**alertaSeverity** | **String** | The severity value for the Alerta service. |  [optional] |
|**alertaStatus** | **String** | The status value for the Alerta service. |  [optional] |
|**alertaTags** | **String** | The comma-separated list of tags for the Alerta service. |  [optional] |
|**alertaType** | **String** | The type value for the Alerta service. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



