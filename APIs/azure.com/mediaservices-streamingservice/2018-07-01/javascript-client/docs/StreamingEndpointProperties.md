# AzureMediaServices.StreamingEndpointProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessControl** | [**StreamingEndpointAccessControl**](StreamingEndpointAccessControl.md) |  | [optional] 
**availabilitySetName** | **String** | The name of the AvailabilitySet used with this StreamingEndpoint for high availability streaming.  This value can only be set at creation time. | [optional] 
**cdnEnabled** | **Boolean** | The CDN enabled flag. | [optional] 
**cdnProfile** | **String** | The CDN profile name. | [optional] 
**cdnProvider** | **String** | The CDN provider name. | [optional] 
**created** | **Date** | The exact time the StreamingEndpoint was created. | [optional] [readonly] 
**crossSiteAccessPolicies** | [**CrossSiteAccessPolicies**](CrossSiteAccessPolicies.md) |  | [optional] 
**customHostNames** | **[String]** | The custom host names of the StreamingEndpoint | [optional] 
**description** | **String** | The StreamingEndpoint description. | [optional] 
**freeTrialEndTime** | **Date** | The free trial expiration time. | [optional] [readonly] 
**hostName** | **String** | The StreamingEndpoint host name. | [optional] [readonly] 
**lastModified** | **Date** | The exact time the StreamingEndpoint was last modified. | [optional] [readonly] 
**maxCacheAge** | **Number** | Max cache age | [optional] 
**provisioningState** | **String** | The provisioning state of the StreamingEndpoint. | [optional] [readonly] 
**resourceState** | **String** | The resource state of the StreamingEndpoint. | [optional] [readonly] 
**scaleUnits** | **Number** | The number of scale units.  Use the Scale operation to adjust this value. | 



## Enum: ResourceStateEnum


* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)

* `Running` (value: `"Running"`)

* `Stopping` (value: `"Stopping"`)

* `Deleting` (value: `"Deleting"`)

* `Scaling` (value: `"Scaling"`)




