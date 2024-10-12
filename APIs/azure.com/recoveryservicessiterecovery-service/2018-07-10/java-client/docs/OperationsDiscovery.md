

# OperationsDiscovery

Operations discovery class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**display** | [**Display**](Display.md) |  |  [optional] |
|**name** | **String** | Name of the API. The name of the operation being performed on this particular object. It should match the action name that appears in RBAC / the event service. Examples of operations include: * Microsoft.Compute/virtualMachine/capture/action * Microsoft.Compute/virtualMachine/restart/action * Microsoft.Compute/virtualMachine/write * Microsoft.Compute/virtualMachine/read * Microsoft.Compute/virtualMachine/delete Each action should include, in order: (1) Resource Provider Namespace (2) Type hierarchy for which the action applies (e.g. server/databases for a SQL Azure database) (3) Read, Write, Action or Delete indicating which type applies. If it is a PUT/PATCH on a collection or named value, Write should be used. If it is a GET, Read should be used. If it is a DELETE, Delete should be used. If it is a POST, Action should be used. As a note: all resource providers would need to include the \&quot;{Resource Provider Namespace}/register/action\&quot; operation in their response. This API is used to register for their service, and should include details about the operation (e.g. a localized name for the resource provider + any special considerations like PII release) |  [optional] |
|**origin** | **String** | Origin. The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. Default value is \&quot;user,system\&quot; |  [optional] |
|**properties** | **Object** | ClientDiscovery properties. |  [optional] |



