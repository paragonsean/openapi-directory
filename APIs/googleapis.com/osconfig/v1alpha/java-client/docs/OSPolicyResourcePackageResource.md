

# OSPolicyResourcePackageResource

A resource that manages a system package.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apt** | [**OSPolicyResourcePackageResourceAPT**](OSPolicyResourcePackageResourceAPT.md) |  |  [optional] |
|**deb** | [**OSPolicyResourcePackageResourceDeb**](OSPolicyResourcePackageResourceDeb.md) |  |  [optional] |
|**desiredState** | [**DesiredStateEnum**](#DesiredStateEnum) | Required. The desired state the agent should maintain for this package. |  [optional] |
|**googet** | [**OSPolicyResourcePackageResourceGooGet**](OSPolicyResourcePackageResourceGooGet.md) |  |  [optional] |
|**msi** | [**OSPolicyResourcePackageResourceMSI**](OSPolicyResourcePackageResourceMSI.md) |  |  [optional] |
|**rpm** | [**OSPolicyResourcePackageResourceRPM**](OSPolicyResourcePackageResourceRPM.md) |  |  [optional] |
|**yum** | [**OSPolicyResourcePackageResourceYUM**](OSPolicyResourcePackageResourceYUM.md) |  |  [optional] |
|**zypper** | [**OSPolicyResourcePackageResourceZypper**](OSPolicyResourcePackageResourceZypper.md) |  |  [optional] |



## Enum: DesiredStateEnum

| Name | Value |
|---- | -----|
| DESIRED_STATE_UNSPECIFIED | &quot;DESIRED_STATE_UNSPECIFIED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| REMOVED | &quot;REMOVED&quot; |



