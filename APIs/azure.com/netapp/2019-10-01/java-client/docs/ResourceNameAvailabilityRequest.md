

# ResourceNameAvailabilityRequest

Resource name availability request content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Resource name to verify. |  |
|**resourceGroup** | **String** | Resource group name. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Resource type used for verification. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NET_APP_ACCOUNTS | &quot;Microsoft.NetApp/netAppAccounts&quot; |
| NET_APP_ACCOUNTS_CAPACITY_POOLS | &quot;Microsoft.NetApp/netAppAccounts/capacityPools&quot; |
| NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES | &quot;Microsoft.NetApp/netAppAccounts/capacityPools/volumes&quot; |
| NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES_SNAPSHOTS | &quot;Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots&quot; |



