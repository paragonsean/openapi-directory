# AppHubApi.Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Attributes**](Attributes.md) |  | [optional] 
**createTime** | **String** | Output only. Create time. | [optional] [readonly] 
**description** | **String** | Optional. User-defined description of a Service. Can have a maximum length of 2048 characters. | [optional] 
**discoveredService** | **String** | Required. Immutable. The resource name of the original discovered service. | [optional] 
**displayName** | **String** | Optional. User-defined name for the Service. Can have a maximum length of 63 characters. | [optional] 
**name** | **String** | Identifier. The resource name of a Service. Format: \&quot;projects/{host-project-id}/locations/{location}/applications/{application-id}/services/{service-id}\&quot; | [optional] 
**serviceProperties** | [**ServiceProperties**](ServiceProperties.md) |  | [optional] 
**serviceReference** | [**ServiceReference**](ServiceReference.md) |  | [optional] 
**state** | **String** | Output only. Service state. | [optional] [readonly] 
**uid** | **String** | Output only. A universally unique identifier (UUID) for the &#x60;Service&#x60; in the UUID4 format. | [optional] [readonly] 
**updateTime** | **String** | Output only. Update time. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `DETACHED` (value: `"DETACHED"`)




