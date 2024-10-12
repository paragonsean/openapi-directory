# OsConfigApi.OSPolicyResourcePackageResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apt** | [**OSPolicyResourcePackageResourceAPT**](OSPolicyResourcePackageResourceAPT.md) |  | [optional] 
**deb** | [**OSPolicyResourcePackageResourceDeb**](OSPolicyResourcePackageResourceDeb.md) |  | [optional] 
**desiredState** | **String** | Required. The desired state the agent should maintain for this package. | [optional] 
**googet** | [**OSPolicyResourcePackageResourceGooGet**](OSPolicyResourcePackageResourceGooGet.md) |  | [optional] 
**msi** | [**OSPolicyResourcePackageResourceMSI**](OSPolicyResourcePackageResourceMSI.md) |  | [optional] 
**rpm** | [**OSPolicyResourcePackageResourceRPM**](OSPolicyResourcePackageResourceRPM.md) |  | [optional] 
**yum** | [**OSPolicyResourcePackageResourceYUM**](OSPolicyResourcePackageResourceYUM.md) |  | [optional] 
**zypper** | [**OSPolicyResourcePackageResourceZypper**](OSPolicyResourcePackageResourceZypper.md) |  | [optional] 



## Enum: DesiredStateEnum


* `DESIRED_STATE_UNSPECIFIED` (value: `"DESIRED_STATE_UNSPECIFIED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `REMOVED` (value: `"REMOVED"`)




