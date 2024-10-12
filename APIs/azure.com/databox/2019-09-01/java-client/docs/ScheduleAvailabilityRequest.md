

# ScheduleAvailabilityRequest

Request body to get the availability for scheduling orders.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**skuName** | [**SkuNameEnum**](#SkuNameEnum) | Sku Name for which the order is to be scheduled. |  |
|**storageLocation** | **String** | Location for data transfer.   For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version&#x3D;2018-01-01 |  |



## Enum: SkuNameEnum

| Name | Value |
|---- | -----|
| DATA_BOX | &quot;DataBox&quot; |
| DATA_BOX_DISK | &quot;DataBoxDisk&quot; |
| DATA_BOX_HEAVY | &quot;DataBoxHeavy&quot; |



