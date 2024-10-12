# FabricAdminClient.DriveModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Detailed recommended action for HealthStatus/OperationalStatus. Empty if HealthStatus/OperationalStatus is Healthy/Ok. | [optional] 
**canPool** | **Boolean** | Indicate whether the drive can be added to the pool. | [optional] 
**cannotPoolReason** | **String** | Specify the reasons why the drive cannot be added to the pool. | [optional] 
**capacityGB** | **Number** | Total capacity in GB of the drive. | [optional] 
**description** | **String** | Detailed description for HealthStatus/OperationalStatus. Empty if HealthStatus/OperationalStatus is Healthy/Ok. | [optional] 
**healthStatus** | **String** | Health status of the drive. | [optional] 
**mediaType** | **String** | Media type of the drive. | [optional] 
**model** | **String** | Model of the drive. | [optional] 
**operationalStatus** | **String** | Operational status of the drive. | [optional] 
**physicalLocation** | **String** | Indicate where the hardware is located. | [optional] 
**serialNumber** | **String** | Serial number of the drive. | [optional] 
**storageNode** | **String** | Node that the drive is physically connected. | [optional] 
**usage** | **String** | Intended usage of the drive. | [optional] 


