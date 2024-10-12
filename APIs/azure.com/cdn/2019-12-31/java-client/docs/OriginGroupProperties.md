

# OriginGroupProperties

The JSON object that contains the properties of the origin group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | Provisioning status of the origin group. |  [optional] [readonly] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) | Resource status of the origin group. |  [optional] [readonly] |
|**healthProbeSettings** | [**HealthProbeParameters**](HealthProbeParameters.md) |  |  [optional] |
|**origins** | [**List&lt;ResourceReference&gt;**](ResourceReference.md) | The source of the content being delivered via CDN within given origin group. |  [optional] |
|**responseBasedOriginErrorDetectionSettings** | [**ResponseBasedOriginErrorDetectionParameters**](ResponseBasedOriginErrorDetectionParameters.md) |  |  [optional] |
|**trafficRestorationTimeToHealedOrNewEndpointsInMinutes** | **Integer** | Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported. |  [optional] |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| ACTIVE | &quot;Active&quot; |
| DELETING | &quot;Deleting&quot; |



