# RecoveryServicesBackupClient.AzureFileshareProtectedItemExtendedInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oldestRecoveryPoint** | **Date** | The oldest backup copy available for this item in the service. | [optional] 
**policyState** | **String** | Indicates consistency of policy object and policy applied to this backup item. | [optional] 
**recoveryPointCount** | **Number** | Number of available backup copies associated with this backup item. | [optional] 
**resourceState** | **String** | Indicates the state of this resource. Possible values are from enum ResourceState {Invalid, Active, SoftDeleted, Deleted} | [optional] [readonly] 
**resourceStateSyncTime** | **Date** | The resource state sync time for this backup item. | [optional] [readonly] 


