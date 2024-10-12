

# ServiceMeshMembershipSpec

**Service Mesh**: Spec for a single Membership for the servicemesh feature

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**controlPlane** | [**ControlPlaneEnum**](#ControlPlaneEnum) | Deprecated: use &#x60;management&#x60; instead Enables automatic control plane management. |  [optional] |
|**management** | [**ManagementEnum**](#ManagementEnum) | Enables automatic Service Mesh management. |  [optional] |



## Enum: ControlPlaneEnum

| Name | Value |
|---- | -----|
| CONTROL_PLANE_MANAGEMENT_UNSPECIFIED | &quot;CONTROL_PLANE_MANAGEMENT_UNSPECIFIED&quot; |
| AUTOMATIC | &quot;AUTOMATIC&quot; |
| MANUAL | &quot;MANUAL&quot; |



## Enum: ManagementEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MANAGEMENT_UNSPECIFIED&quot; |
| AUTOMATIC | &quot;MANAGEMENT_AUTOMATIC&quot; |
| MANUAL | &quot;MANAGEMENT_MANUAL&quot; |



