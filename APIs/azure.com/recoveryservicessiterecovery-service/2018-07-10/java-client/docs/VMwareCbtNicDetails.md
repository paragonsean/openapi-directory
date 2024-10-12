

# VMwareCbtNicDetails

VMwareCbt NIC details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isPrimaryNic** | **String** | A value indicating whether this is the primary NIC. |  [optional] |
|**isSelectedForMigration** | **String** | A value indicating whether this NIC is selected for migration. |  [optional] |
|**nicId** | **String** | The NIC Id. |  [optional] [readonly] |
|**sourceIPAddress** | **String** | The source IP address. |  [optional] [readonly] |
|**sourceIPAddressType** | [**SourceIPAddressTypeEnum**](#SourceIPAddressTypeEnum) | The source IP address type. |  [optional] [readonly] |
|**sourceNetworkId** | **String** | Source network Id. |  [optional] [readonly] |
|**targetIPAddress** | **String** | The target IP address. |  [optional] |
|**targetIPAddressType** | [**TargetIPAddressTypeEnum**](#TargetIPAddressTypeEnum) | The target IP address type. |  [optional] |
|**targetSubnetName** | **String** | Target subnet name. |  [optional] |



## Enum: SourceIPAddressTypeEnum

| Name | Value |
|---- | -----|
| DYNAMIC | &quot;Dynamic&quot; |
| STATIC | &quot;Static&quot; |



## Enum: TargetIPAddressTypeEnum

| Name | Value |
|---- | -----|
| DYNAMIC | &quot;Dynamic&quot; |
| STATIC | &quot;Static&quot; |



