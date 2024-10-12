

# GoogleApiService

`Service` is the root object of Google API service configuration (service config). It describes the basic information about a logical service, such as the service name and the user-facing title, and delegates other aspects to sub-sections. Each sub-section is either a proto message or a repeated proto message that configures a specific aspect, such as auth. For more information, see each proto message definition. Example: type: google.api.Service name: calendar.googleapis.com title: Google Calendar API apis: - name: google.calendar.v3.Calendar visibility: rules: - selector: \"google.calendar.v3.*\" restriction: PREVIEW backend: rules: - selector: \"google.calendar.v3.*\" address: calendar.example.com authentication: providers: - id: google_calendar_auth jwks_uri: https://www.googleapis.com/oauth2/v1/certs issuer: https://securetoken.google.com rules: - selector: \"*\" requirements: provider_id: google_calendar_auth

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apis** | [**List&lt;Api&gt;**](Api.md) | A list of API interfaces exported by this service. Only the &#x60;name&#x60; field of the google.protobuf.Api needs to be provided by the configuration author, as the remaining fields will be derived from the IDL during the normalization process. It is an error to specify an API interface here which cannot be resolved against the associated IDL files. |  [optional] |
|**authentication** | [**Authentication**](Authentication.md) |  |  [optional] |
|**backend** | [**Backend**](Backend.md) |  |  [optional] |
|**billing** | [**Billing**](Billing.md) |  |  [optional] |
|**configVersion** | **Integer** | Obsolete. Do not use. This field has no semantic meaning. The service config compiler always sets this field to &#x60;3&#x60;. |  [optional] |
|**context** | [**Context**](Context.md) |  |  [optional] |
|**control** | [**Control**](Control.md) |  |  [optional] |
|**customError** | [**CustomError**](CustomError.md) |  |  [optional] |
|**documentation** | [**Documentation**](Documentation.md) |  |  [optional] |
|**endpoints** | [**List&lt;Endpoint&gt;**](Endpoint.md) | Configuration for network endpoints. If this is empty, then an endpoint with the same name as the service is automatically generated to service all defined APIs. |  [optional] |
|**enums** | [**List&lt;ModelEnum&gt;**](ModelEnum.md) | A list of all enum types included in this API service. Enums referenced directly or indirectly by the &#x60;apis&#x60; are automatically included. Enums which are not referenced but shall be included should be listed here by name by the configuration author. Example: enums: - name: google.someapi.v1.SomeEnum |  [optional] |
|**http** | [**Http**](Http.md) |  |  [optional] |
|**id** | **String** | A unique ID for a specific instance of this message, typically assigned by the client for tracking purpose. Must be no longer than 63 characters and only lower case letters, digits, &#39;.&#39;, &#39;_&#39; and &#39;-&#39; are allowed. If empty, the server may choose to generate one instead. |  [optional] |
|**logging** | [**Logging**](Logging.md) |  |  [optional] |
|**logs** | [**List&lt;LogDescriptor&gt;**](LogDescriptor.md) | Defines the logs used by this service. |  [optional] |
|**metrics** | [**List&lt;MetricDescriptor&gt;**](MetricDescriptor.md) | Defines the metrics used by this service. |  [optional] |
|**monitoredResources** | [**List&lt;MonitoredResourceDescriptor&gt;**](MonitoredResourceDescriptor.md) | Defines the monitored resources used by this service. This is required by the Service.monitoring and Service.logging configurations. |  [optional] |
|**monitoring** | [**Monitoring**](Monitoring.md) |  |  [optional] |
|**name** | **String** | The service name, which is a DNS-like logical identifier for the service, such as &#x60;calendar.googleapis.com&#x60;. The service name typically goes through DNS verification to make sure the owner of the service also owns the DNS name. |  [optional] |
|**producerProjectId** | **String** | The Google project that owns this service. |  [optional] |
|**publishing** | [**Publishing**](Publishing.md) |  |  [optional] |
|**quota** | [**Quota**](Quota.md) |  |  [optional] |
|**sourceInfo** | [**SourceInfo**](SourceInfo.md) |  |  [optional] |
|**systemParameters** | [**SystemParameters**](SystemParameters.md) |  |  [optional] |
|**systemTypes** | [**List&lt;Type&gt;**](Type.md) | A list of all proto message types included in this API service. It serves similar purpose as [google.api.Service.types], except that these types are not needed by user-defined APIs. Therefore, they will not show up in the generated discovery doc. This field should only be used to define system APIs in ESF. |  [optional] |
|**title** | **String** | The product title for this service, it is the name displayed in Google Cloud Console. |  [optional] |
|**types** | [**List&lt;Type&gt;**](Type.md) | A list of all proto message types included in this API service. Types referenced directly or indirectly by the &#x60;apis&#x60; are automatically included. Messages which are not referenced but shall be included, such as types used by the &#x60;google.protobuf.Any&#x60; type, should be listed here by name by the configuration author. Example: types: - name: google.protobuf.Int32 |  [optional] |
|**usage** | [**Usage**](Usage.md) |  |  [optional] |



