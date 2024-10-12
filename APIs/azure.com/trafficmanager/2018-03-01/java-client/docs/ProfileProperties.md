

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
|**trafficViewEnrollmentStatus** | [**TrafficViewEnrollmentStatusEnum**](#TrafficViewEnrollmentStatusEnum) | Indicates whether Traffic View is &#39;Enabled&#39; or &#39;Disabled&#39; for the Traffic Manager profile. Null, indicates &#39;Disabled&#39;. Enabling this feature will increase the cost of the Traffic Manage profile. |  [optional] |



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



## Enum: TrafficViewEnrollmentStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



