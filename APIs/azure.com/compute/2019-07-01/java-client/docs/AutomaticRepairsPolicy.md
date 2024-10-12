

# AutomaticRepairsPolicy

Specifies the configuration parameters for automatic repairs on the virtual machine scale set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Specifies whether automatic repairs should be enabled on the virtual machine scale set. The default value is false. |  [optional] |
|**gracePeriod** | **String** | The amount of time for which automatic repairs are suspended due to a state change on VM. The grace time starts after the state change has completed. This helps avoid premature or accidental repairs. The time duration should be specified in ISO 8601 format. The minimum allowed grace period is 30 minutes (PT30M), which is also the default value. |  [optional] |



