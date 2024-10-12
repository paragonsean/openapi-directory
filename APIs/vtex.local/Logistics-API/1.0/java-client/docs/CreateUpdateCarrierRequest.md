

# CreateUpdateCarrierRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierSchedule** | **List&lt;String&gt;** |  |  |
|**dayOfWeekBlockeds** | **List&lt;String&gt;** |  |  |
|**dayOfWeekForDelivery** | [**List&lt;DayOfWeekForDeliveryInner&gt;**](DayOfWeekForDeliveryInner.md) | Select the chosen days for delivery. Values for each day of the week are: 0 &#x3D; sunday, 1 &#x3D; monday, 2 &#x3D; tuesday, 3 &#x3D; wednesday, 4 &#x3D; thursday, 5 &#x3D; friday, 6 &#x3D; saturday. Make sure to add the available hours for the chosen days, following the example. |  |
|**deliveryOnWeekends** | **Boolean** |  |  |
|**exclusiveToDeliveryPoints** | **Boolean** |  |  |
|**factorCubicWeight** | **String** |  |  |
|**freightTableProcessStatus** | **Integer** |  |  |
|**freightTableValueError** | **String** |  |  |
|**freightValue** | **List&lt;String&gt;** |  |  |
|**id** | **String** |  |  |
|**isPolygon** | **Boolean** |  |  |
|**maxDimension** | [**MaxDimension1**](MaxDimension1.md) |  |  |
|**maxRangeDelivery** | **Integer** |  |  |
|**minimunCubicWeight** | **Integer** |  |  |
|**modals** | **List&lt;String&gt;** |  |  |
|**name** | **String** |  |  |
|**numberOfItemsPerShipment** | **String** |  |  |
|**onlyItemsWithDefinedModal** | **Boolean** |  |  |
|**scheduledDelivery** | **Boolean** |  |  |
|**slaType** | **String** |  |  |



