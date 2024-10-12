

# ServiceMeshMembershipSpec

**Service Mesh**: Spec for a single Membership for the servicemesh feature

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**controlPlane** | [**ControlPlaneEnum**](#ControlPlaneEnum) | Deprecated: use &#x60;management&#x60; instead Enables automatic control plane management. |  [optional] |
|**defaultChannel** | [**DefaultChannelEnum**](#DefaultChannelEnum) | Determines which release channel to use for default injection and service mesh APIs. |  [optional] |
|**management** | [**ManagementEnum**](#ManagementEnum) | Enables automatic Service Mesh management. |  [optional] |



## Enum: ControlPlaneEnum

| Name | Value |
|---- | -----|
| CONTROL_PLANE_MANAGEMENT_UNSPECIFIED | &quot;CONTROL_PLANE_MANAGEMENT_UNSPECIFIED&quot; |
| AUTOMATIC | &quot;AUTOMATIC&quot; |
| MANUAL | &quot;MANUAL&quot; |



## Enum: DefaultChannelEnum

| Name | Value |
|---- | -----|
| CHANNEL_UNSPECIFIED | &quot;CHANNEL_UNSPECIFIED&quot; |
| RAPID | &quot;RAPID&quot; |
| REGULAR | &quot;REGULAR&quot; |
| STABLE | &quot;STABLE&quot; |



## Enum: ManagementEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MANAGEMENT_UNSPECIFIED&quot; |
| AUTOMATIC | &quot;MANAGEMENT_AUTOMATIC&quot; |
| MANUAL | &quot;MANAGEMENT_MANUAL&quot; |



