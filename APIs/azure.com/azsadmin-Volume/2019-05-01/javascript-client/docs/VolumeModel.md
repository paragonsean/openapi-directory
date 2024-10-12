# FabricAdminClient.VolumeModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Detailed recommended action for HealthStatus/OperationalStatus. Empty if HealthStatus/OperationalStatus is Healthy/Ok. | [optional] [readonly] 
**description** | **String** | Detailed description for HealthStatus/OperationalStatus. Empty if HealthStatus/OperationalStatus is Healthy/Ok. | [optional] [readonly] 
**healthStatus** | **String** | Health status of the volume. | [optional] [readonly] 
**operationalStatus** | **String** | Operational status of the volume. | [optional] [readonly] 
**remainingCapacityGB** | **Number** | Remaining capacity in GB of the volume. | [optional] [readonly] 
**repairStatus** | **String** | Repair status of the volume. Empty if no repair job running, something like &#39;Running, 90%&#39; when repairing. | [optional] [readonly] 
**totalCapacityGB** | **Number** | Total capacity in GB of the volume. | [optional] [readonly] 
**volumeLabel** | **String** | Volume label. | [optional] [readonly] 


