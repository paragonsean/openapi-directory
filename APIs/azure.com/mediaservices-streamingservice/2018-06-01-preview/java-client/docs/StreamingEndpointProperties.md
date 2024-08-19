

# StreamingEndpointProperties

The StreamingEndpoint properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessControl** | [**StreamingEndpointAccessControl**](StreamingEndpointAccessControl.md) |  |  [optional] |
|**availabilitySetName** | **String** | AvailabilitySet name |  [optional] |
|**cdnEnabled** | **Boolean** | The CDN enabled flag. |  [optional] |
|**cdnProfile** | **String** | The CDN profile name. |  [optional] |
|**cdnProvider** | **String** | The CDN provider name. |  [optional] |
|**created** | **OffsetDateTime** | The exact time the StreamingEndpoint was created. |  [optional] [readonly] |
|**crossSiteAccessPolicies** | [**CrossSiteAccessPolicies**](CrossSiteAccessPolicies.md) |  |  [optional] |
|**customHostNames** | **List&lt;String&gt;** | The custom host names of the StreamingEndpoint |  [optional] |
|**description** | **String** | The StreamingEndpoint description. |  [optional] |
|**freeTrialEndTime** | **OffsetDateTime** | The free trial expiration time. |  [optional] [readonly] |
|**hostName** | **String** | The StreamingEndpoint host name. |  [optional] [readonly] |
|**lastModified** | **OffsetDateTime** | The exact time the StreamingEndpoint was last modified. |  [optional] [readonly] |
|**maxCacheAge** | **Long** | Max cache age |  [optional] |
|**provisioningState** | **String** | The provisioning state of the StreamingEndpoint. |  [optional] [readonly] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) | The resource state of the StreamingEndpoint. |  [optional] [readonly] |
|**scaleUnits** | **Integer** | The number of scale units. |  [optional] |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |
| DELETING | &quot;Deleting&quot; |
| SCALING | &quot;Scaling&quot; |



