

# OSPolicyResource

An OS policy resource is used to define the desired state configuration and provides a specific functionality like installing/removing packages, executing a script etc. The system ensures that resources are always in their desired state by taking necessary actions if they have drifted from their desired state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exec** | [**OSPolicyResourceExecResource**](OSPolicyResourceExecResource.md) |  |  [optional] |
|**_file** | [**OSPolicyResourceFileResource**](OSPolicyResourceFileResource.md) |  |  [optional] |
|**id** | **String** | Required. The id of the resource with the following restrictions: * Must contain only lowercase letters, numbers, and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the OS policy. |  [optional] |
|**pkg** | [**OSPolicyResourcePackageResource**](OSPolicyResourcePackageResource.md) |  |  [optional] |
|**repository** | [**OSPolicyResourceRepositoryResource**](OSPolicyResourceRepositoryResource.md) |  |  [optional] |



