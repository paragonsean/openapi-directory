# CdnManagementClient.DeepCreatedOriginGroupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthProbeSettings** | [**HealthProbeParameters**](HealthProbeParameters.md) |  | [optional] 
**origins** | [**[ResourceReference]**](ResourceReference.md) | The source of the content being delivered via CDN within given origin group. | 
**responseBasedOriginErrorDetectionSettings** | [**ResponseBasedOriginErrorDetectionParameters**](ResponseBasedOriginErrorDetectionParameters.md) |  | [optional] 
**trafficRestorationTimeToHealedOrNewEndpointsInMinutes** | **Number** | Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported. | [optional] 


