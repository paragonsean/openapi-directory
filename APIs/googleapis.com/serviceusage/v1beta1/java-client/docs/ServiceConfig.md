

# ServiceConfig

The configuration of the service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apis** | [**List&lt;Api&gt;**](Api.md) | A list of API interfaces exported by this service. Contains only the names, versions, and method names of the interfaces. |  [optional] |
|**authentication** | [**Authentication**](Authentication.md) |  |  [optional] |
|**documentation** | [**Documentation**](Documentation.md) |  |  [optional] |
|**endpoints** | [**List&lt;Endpoint&gt;**](Endpoint.md) | Configuration for network endpoints. Contains only the names and aliases of the endpoints. |  [optional] |
|**monitoredResources** | [**List&lt;MonitoredResourceDescriptor&gt;**](MonitoredResourceDescriptor.md) | Defines the monitored resources used by this service. This is required by the Service.monitoring and Service.logging configurations. |  [optional] |
|**monitoring** | [**Monitoring**](Monitoring.md) |  |  [optional] |
|**name** | **String** | The DNS address at which this service is available. An example DNS address would be: &#x60;calendar.googleapis.com&#x60;. |  [optional] |
|**quota** | [**Quota**](Quota.md) |  |  [optional] |
|**title** | **String** | The product title for this service. |  [optional] |
|**usage** | [**Usage**](Usage.md) |  |  [optional] |



