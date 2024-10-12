

# RoleValues

This structure defines which groups defined in the SAML assertion attribute are to be mapped to the Grafana <code>Admin</code> and <code>Editor</code> roles in the workspace. SAML authenticated users not part of <code>Admin</code> or <code>Editor</code> role groups have <code>Viewer</code> permission over the workspace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**admin** | [**List**](List.md) |  |  [optional] |
|**editor** | [**List**](List.md) |  |  [optional] |



