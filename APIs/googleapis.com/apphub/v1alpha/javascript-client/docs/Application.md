# AppHubApi.Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Attributes**](Attributes.md) |  | [optional] 
**createTime** | **String** | Output only. Create time. | [optional] [readonly] 
**description** | **String** | Optional. User-defined description of an Application. Can have a maximum length of 2048 characters. | [optional] 
**displayName** | **String** | Optional. User-defined name for the Application. Can have a maximum length of 63 characters. | [optional] 
**name** | **String** | Identifier. The resource name of an Application. Format: \&quot;projects/{host-project-id}/locations/{location}/applications/{application-id}\&quot; | [optional] 
**scope** | [**Scope**](Scope.md) |  | [optional] 
**state** | **String** | Output only. Application state. | [optional] [readonly] 
**uid** | **String** | Output only. A universally unique identifier (in UUID4 format) for the &#x60;Application&#x60;. | [optional] [readonly] 
**updateTime** | **String** | Output only. Update time. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)




