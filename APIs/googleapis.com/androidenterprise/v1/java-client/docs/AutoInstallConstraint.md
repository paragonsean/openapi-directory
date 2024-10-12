

# AutoInstallConstraint

The auto-install constraint. Defines a set of restrictions for installation. At least one of the fields must be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chargingStateConstraint** | [**ChargingStateConstraintEnum**](#ChargingStateConstraintEnum) | Charging state constraint. |  [optional] |
|**deviceIdleStateConstraint** | [**DeviceIdleStateConstraintEnum**](#DeviceIdleStateConstraintEnum) | Device idle state constraint. |  [optional] |
|**networkTypeConstraint** | [**NetworkTypeConstraintEnum**](#NetworkTypeConstraintEnum) | Network type constraint. |  [optional] |



## Enum: ChargingStateConstraintEnum

| Name | Value |
|---- | -----|
| CHARGING_STATE_CONSTRAINT_UNSPECIFIED | &quot;chargingStateConstraintUnspecified&quot; |
| CHARGING_NOT_REQUIRED | &quot;chargingNotRequired&quot; |
| CHARGING_REQUIRED | &quot;chargingRequired&quot; |



## Enum: DeviceIdleStateConstraintEnum

| Name | Value |
|---- | -----|
| DEVICE_IDLE_STATE_CONSTRAINT_UNSPECIFIED | &quot;deviceIdleStateConstraintUnspecified&quot; |
| DEVICE_IDLE_NOT_REQUIRED | &quot;deviceIdleNotRequired&quot; |
| DEVICE_IDLE_REQUIRED | &quot;deviceIdleRequired&quot; |



## Enum: NetworkTypeConstraintEnum

| Name | Value |
|---- | -----|
| NETWORK_TYPE_CONSTRAINT_UNSPECIFIED | &quot;networkTypeConstraintUnspecified&quot; |
| ANY_NETWORK | &quot;anyNetwork&quot; |
| UNMETERED_NETWORK | &quot;unmeteredNetwork&quot; |



