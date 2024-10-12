# AzureMigrateV2.Machine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eTag** | **String** | For optimistic concurrency control. | [optional] 
**id** | **String** | Path reference to this machine. /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/machines/{machineName} | [optional] [readonly] 
**name** | **String** | Name of the machine. It is a GUID which is unique identifier of machine in private data center. For user-readable name, we have a displayName property on this machine. | [optional] [readonly] 
**properties** | [**MachineProperties**](MachineProperties.md) |  | [optional] 
**type** | **String** | Type of the object &#x3D; [Microsoft.Migrate/assessmentProjects/machines]. | [optional] [readonly] 


