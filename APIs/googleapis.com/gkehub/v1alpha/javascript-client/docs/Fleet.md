# GkeHubApi.Fleet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. When the Fleet was created. | [optional] [readonly] 
**defaultClusterConfig** | [**DefaultClusterConfig**](DefaultClusterConfig.md) |  | [optional] 
**deleteTime** | **String** | Output only. When the Fleet was deleted. | [optional] [readonly] 
**displayName** | **String** | Optional. A user-assigned display name of the Fleet. When present, it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: &#x60;Production Fleet&#x60; | [optional] 
**labels** | **{String: String}** | Optional. Labels for this Fleet. | [optional] 
**name** | **String** | Output only. The full, unique resource name of this fleet in the format of &#x60;projects/{project}/locations/{location}/fleets/{fleet}&#x60;. Each Google Cloud project can have at most one fleet resource, named \&quot;default\&quot;. | [optional] [readonly] 
**state** | [**FleetLifecycleState**](FleetLifecycleState.md) |  | [optional] 
**uid** | **String** | Output only. Google-generated UUID for this resource. This is unique across all Fleet resources. If a Fleet resource is deleted and another resource with the same name is created, it gets a different uid. | [optional] [readonly] 
**updateTime** | **String** | Output only. When the Fleet was last updated. | [optional] [readonly] 


