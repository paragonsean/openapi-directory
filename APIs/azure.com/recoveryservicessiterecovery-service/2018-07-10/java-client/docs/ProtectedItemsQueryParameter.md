

# ProtectedItemsQueryParameter

Query parameter to enumerate protected items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceType** | **String** | The replication provider type. |  [optional] |
|**multiVmGroupCreateOption** | [**MultiVmGroupCreateOptionEnum**](#MultiVmGroupCreateOptionEnum) | Whether Multi VM group is auto created or specified by user. |  [optional] |
|**recoveryPlanName** | **String** | The recovery plan filter. |  [optional] |
|**sourceFabricName** | **String** | The source fabric name filter. |  [optional] |
|**vCenterName** | **String** | The vCenter name filter. |  [optional] |



## Enum: MultiVmGroupCreateOptionEnum

| Name | Value |
|---- | -----|
| AUTO_CREATED | &quot;AutoCreated&quot; |
| USER_SPECIFIED | &quot;UserSpecified&quot; |



