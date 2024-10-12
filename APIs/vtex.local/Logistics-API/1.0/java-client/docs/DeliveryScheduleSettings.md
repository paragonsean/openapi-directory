

# DeliveryScheduleSettings

Settings for the Scheduled Delivery feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeekForDelivery** | [**List&lt;DayOfWeekForDeliveryInner&gt;**](DayOfWeekForDeliveryInner.md) | Select the chosen days for delivery. Values for each day of the week are: 0 &#x3D; sunday, 1 &#x3D; monday, 2 &#x3D; tuesday, 3 &#x3D; wednesday, 4 &#x3D; thursday, 5 &#x3D; friday, 6 &#x3D; saturday. Make sure to add the available hours for the chosen days, following the example. |  |
|**maxRangeDelivery** | **BigDecimal** | Range of days available within a delivery window, for the customer to choose the scheduled delivery. For example, if the configured maxRangeDelivery is equal 7, and the customer buys something on a Tuesday, the options for scheduled delivery will be shown until the following Tuesday (7 days from the purchase day). If no options are available within the maxRangeDelivery set, this shipping policy won&#39;t be shown on the checkout. |  |
|**useDeliverySchedule** | **Boolean** | Select the Scheduled Delivery configuration. |  |



