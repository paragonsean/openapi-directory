

# AvailableProviderOperation

Class represents provider operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**display** | [**AvailableProviderOperationDisplay**](AvailableProviderOperationDisplay.md) |  |  [optional] |
|**name** | **String** | Gets or sets the name of the operation being performed on this particular object  Return value format: \&quot;{resourceProviderNamespace}/{resourceType}/{read|write|deletion|action}\&quot;  Eg: Microsoft.StorSimple/managers/devices/fileServers/read      Microsoft.StorSimple/managers/devices/alerts/clearAlerts/action |  [optional] |
|**origin** | **String** | Gets or sets Origin  The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX.  Default value is “user,system” |  [optional] |
|**properties** | **Object** | Class represents Properties in AvailableProviderOperations |  [optional] |



