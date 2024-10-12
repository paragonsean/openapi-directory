# ManagedLabsClient.EnvironmentDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the Environment | [optional] [readonly] 
**environmentState** | **String** | Publishing state of the environment setting Possible values are Creating, Created, Failed | [optional] [readonly] 
**id** | **String** | Resource Id of the environment | [optional] [readonly] 
**latestOperationResult** | [**LatestOperationResult**](LatestOperationResult.md) |  | [optional] 
**name** | **String** | Name of the Environment | [optional] [readonly] 
**passwordLastReset** | **Date** | When the password was last reset on the environment. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the environment. This also includes LabIsFull and NotYetProvisioned status. | [optional] [readonly] 
**totalUsage** | **String** | How long the environment has been used by a lab user | [optional] [readonly] 
**virtualMachineDetails** | [**VirtualMachineDetails**](VirtualMachineDetails.md) |  | [optional] 


