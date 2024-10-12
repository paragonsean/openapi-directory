

# ProfileProperties

Class representing the Traffic Manager profile properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsConfig** | [**DnsConfig**](DnsConfig.md) |  |  [optional] |
|**endpoints** | [**List&lt;Endpoint&gt;**](Endpoint.md) | The list of endpoints in the Traffic Manager profile. |  [optional] |
|**monitorConfig** | [**MonitorConfig**](MonitorConfig.md) |  |  [optional] |
|**profileStatus** | [**ProfileStatusEnum**](#ProfileStatusEnum) | The status of the Traffic Manager profile. |  [optional] |
|**trafficRoutingMethod** | [**TrafficRoutingMethodEnum**](#TrafficRoutingMethodEnum) | The traffic routing method of the Traffic Manager profile. |  [optional] |



## Enum: ProfileStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: TrafficRoutingMethodEnum

| Name | Value |
|---- | -----|
| PERFORMANCE | &quot;Performance&quot; |
| PRIORITY | &quot;Priority&quot; |
| WEIGHTED | &quot;Weighted&quot; |
| GEOGRAPHIC | &quot;Geographic&quot; |



