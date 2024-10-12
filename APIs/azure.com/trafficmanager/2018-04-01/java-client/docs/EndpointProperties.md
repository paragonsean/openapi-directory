

# EndpointProperties

Class representing a Traffic Manager endpoint properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customHeaders** | [**List&lt;EndpointPropertiesCustomHeadersInner&gt;**](EndpointPropertiesCustomHeadersInner.md) | List of custom headers. |  [optional] |
|**endpointLocation** | **String** | Specifies the location of the external or nested endpoints when using the &#39;Performance&#39; traffic routing method. |  [optional] |
|**endpointMonitorStatus** | [**EndpointMonitorStatusEnum**](#EndpointMonitorStatusEnum) | The monitoring status of the endpoint. |  [optional] |
|**endpointStatus** | [**EndpointStatusEnum**](#EndpointStatusEnum) | The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method. |  [optional] |
|**geoMapping** | **List&lt;String&gt;** | The list of countries/regions mapped to this endpoint when using the &#39;Geographic&#39; traffic routing method. Please consult Traffic Manager Geographic documentation for a full list of accepted values. |  [optional] |
|**minChildEndpoints** | **Long** | The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type &#39;NestedEndpoints&#39;. |  [optional] |
|**priority** | **Long** | The priority of this endpoint when using the &#39;Priority&#39; traffic routing method. Possible values are from 1 to 1000, lower values represent higher priority. This is an optional parameter.  If specified, it must be specified on all endpoints, and no two endpoints can share the same priority value. |  [optional] |
|**subnets** | [**List&lt;EndpointPropertiesSubnetsInner&gt;**](EndpointPropertiesSubnetsInner.md) | The list of subnets, IP addresses, and/or address ranges mapped to this endpoint when using the &#39;Subnet&#39; traffic routing method. An empty list will match all ranges not covered by other endpoints. |  [optional] |
|**target** | **String** | The fully-qualified DNS name or IP address of the endpoint. Traffic Manager returns this value in DNS responses to direct traffic to this endpoint. |  [optional] |
|**targetResourceId** | **String** | The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type &#39;ExternalEndpoints&#39;. |  [optional] |
|**weight** | **Long** | The weight of this endpoint when using the &#39;Weighted&#39; traffic routing method. Possible values are from 1 to 1000. |  [optional] |



## Enum: EndpointMonitorStatusEnum

| Name | Value |
|---- | -----|
| CHECKING_ENDPOINT | &quot;CheckingEndpoint&quot; |
| ONLINE | &quot;Online&quot; |
| DEGRADED | &quot;Degraded&quot; |
| DISABLED | &quot;Disabled&quot; |
| INACTIVE | &quot;Inactive&quot; |
| STOPPED | &quot;Stopped&quot; |



## Enum: EndpointStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



