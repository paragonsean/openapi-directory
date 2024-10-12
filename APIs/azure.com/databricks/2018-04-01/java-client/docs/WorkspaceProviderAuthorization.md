

# WorkspaceProviderAuthorization

The workspace provider authorization.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **UUID** | The provider&#39;s principal identifier. This is the identity that the provider will use to call ARM to manage the workspace resources. |  |
|**roleDefinitionId** | **UUID** | The provider&#39;s role definition identifier. This role will define all the permissions that the provider must have on the workspace&#39;s container resource group. This role definition cannot have permission to delete the resource group. |  |



