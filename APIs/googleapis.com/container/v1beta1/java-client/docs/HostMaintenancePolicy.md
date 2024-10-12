

# HostMaintenancePolicy

HostMaintenancePolicy contains the maintenance policy for the hosts on which the GKE VMs run on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maintenanceInterval** | [**MaintenanceIntervalEnum**](#MaintenanceIntervalEnum) | Specifies the frequency of planned maintenance events. |  [optional] |
|**opportunisticMaintenanceStrategy** | [**OpportunisticMaintenanceStrategy**](OpportunisticMaintenanceStrategy.md) |  |  [optional] |



## Enum: MaintenanceIntervalEnum

| Name | Value |
|---- | -----|
| MAINTENANCE_INTERVAL_UNSPECIFIED | &quot;MAINTENANCE_INTERVAL_UNSPECIFIED&quot; |
| AS_NEEDED | &quot;AS_NEEDED&quot; |
| PERIODIC | &quot;PERIODIC&quot; |



