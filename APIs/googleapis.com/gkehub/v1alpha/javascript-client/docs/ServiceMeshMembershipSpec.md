# GkeHubApi.ServiceMeshMembershipSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controlPlane** | **String** | Deprecated: use &#x60;management&#x60; instead Enables automatic control plane management. | [optional] 
**defaultChannel** | **String** | Determines which release channel to use for default injection and service mesh APIs. | [optional] 
**management** | **String** | Enables automatic Service Mesh management. | [optional] 



## Enum: ControlPlaneEnum


* `CONTROL_PLANE_MANAGEMENT_UNSPECIFIED` (value: `"CONTROL_PLANE_MANAGEMENT_UNSPECIFIED"`)

* `AUTOMATIC` (value: `"AUTOMATIC"`)

* `MANUAL` (value: `"MANUAL"`)





## Enum: DefaultChannelEnum


* `CHANNEL_UNSPECIFIED` (value: `"CHANNEL_UNSPECIFIED"`)

* `RAPID` (value: `"RAPID"`)

* `REGULAR` (value: `"REGULAR"`)

* `STABLE` (value: `"STABLE"`)





## Enum: ManagementEnum


* `UNSPECIFIED` (value: `"MANAGEMENT_UNSPECIFIED"`)

* `AUTOMATIC` (value: `"MANAGEMENT_AUTOMATIC"`)

* `MANUAL` (value: `"MANAGEMENT_MANUAL"`)




