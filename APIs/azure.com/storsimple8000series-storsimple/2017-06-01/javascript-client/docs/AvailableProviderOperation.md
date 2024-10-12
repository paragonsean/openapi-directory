# StorSimple8000SeriesManagementClient.AvailableProviderOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | [**AvailableProviderOperationDisplay**](AvailableProviderOperationDisplay.md) |  | [optional] 
**name** | **String** | The name of the operation being performed on a particular object. Name format: \&quot;{resourceProviderNamespace}/{resourceType}/{read|write|delete|action}\&quot;. Eg. Microsoft.StorSimple/managers/devices/volumeContainers/read, Microsoft.StorSimple/managers/devices/alerts/clearAlerts/action | [optional] 
**origin** | **String** | The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. Default value is \&quot;user,system\&quot; | [optional] 
**properties** | **Object** | Represents properties of AvailableProviderOperation | [optional] 


