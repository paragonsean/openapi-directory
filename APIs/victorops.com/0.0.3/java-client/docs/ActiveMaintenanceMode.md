

# ActiveMaintenanceMode


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceId** | **String** | external friendly unique id for maintenance mode |  [optional] |
|**isGlobal** | **Boolean** | whether this instance is a global maintenance mode or for specific routing keys |  [optional] |
|**startedAt** | **BigDecimal** | millis from epoch marking the start time |  [optional] |
|**startedBy** | **String** | username of the user that started maintenance mode |  [optional] |
|**targets** | [**List&lt;MaintenanceModeTarget&gt;**](MaintenanceModeTarget.md) |  |  [optional] |



