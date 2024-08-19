# TrafficManagerManagementClient.EndpointProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpointLocation** | **String** | Specifies the location of the external or nested endpoints when using the ‘Performance’ traffic routing method. | [optional] 
**endpointMonitorStatus** | **String** | The monitoring status of the endpoint. | [optional] 
**endpointStatus** | **String** | The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method. | [optional] 
**geoMapping** | **[String]** | The list of countries/regions mapped to this endpoint when using the ‘Geographic’ traffic routing method. Please consult Traffic Manager Geographic documentation for a full list of accepted values. | [optional] 
**minChildEndpoints** | **Number** | The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type &#39;NestedEndpoints&#39;. | [optional] 
**priority** | **Number** | The priority of this endpoint when using the ‘Priority’ traffic routing method. Possible values are from 1 to 1000, lower values represent higher priority. This is an optional parameter.  If specified, it must be specified on all endpoints, and no two endpoints can share the same priority value. | [optional] 
**target** | **String** | The fully-qualified DNS name of the endpoint. Traffic Manager returns this value in DNS responses to direct traffic to this endpoint. | [optional] 
**targetResourceId** | **String** | The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type &#39;ExternalEndpoints&#39;. | [optional] 
**weight** | **Number** | The weight of this endpoint when using the &#39;Weighted&#39; traffic routing method. Possible values are from 1 to 1000. | [optional] 



## Enum: EndpointMonitorStatusEnum


* `CheckingEndpoint` (value: `"CheckingEndpoint"`)

* `Online` (value: `"Online"`)

* `Degraded` (value: `"Degraded"`)

* `Disabled` (value: `"Disabled"`)

* `Inactive` (value: `"Inactive"`)

* `Stopped` (value: `"Stopped"`)





## Enum: EndpointStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




