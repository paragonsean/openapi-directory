

# GetVehicleChargestate200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batteryCapacity** | **BigDecimal** | Vehicle&#39;s maximum physical battery capacity in kWh. This number slowly decreases/degrades over time. |  [optional] |
|**batteryLevel** | **BigDecimal** | Remaining battery in percent |  [optional] |
|**chargeLimit** | **BigDecimal** | Charge limit, as a percent of &#x60;batteryCapacity&#x60;. |  [optional] |
|**chargeRate** | **BigDecimal** | The current charge rate in kW.  This property is only available when the vehicle is charging, and is &#x60;null&#x60; any other time. |  [optional] |
|**chargeTimeRemaining** | **BigDecimal** | Estimated time until the current charging intent is completed, in minutes.  This property is only available when the vehicle is charging, and is &#x60;null&#x60; any other time. |  [optional] |
|**isCharging** | **Boolean** | Current charging status of the vehicle |  [optional] |
|**isChargingReasons** | [**List&lt;IsChargingReasonsEnum&gt;**](#List&lt;IsChargingReasonsEnum&gt;) | Array of string constants that explain why the car is or is not charging. May contain multiple values.  **Any:** - DEFAULT - the car is not being controlled by Enode  **Not Charging:** - NOT_PLUGGED_IN - because the car is not plugged into a charger - FULLY_CHARGED - because the car is fully charged - MANUALLY_STOPPED - because the car has been manually commanded to stop charging - SMART_CHARGING_DELAY - because Smart Charging has identified an opportunity to delay charging until prices are lower  **Charging:** - MANUALLY_STARTED - because the car has been manually commanded to start charging - SMART_CHARGING_ACTIVE - because Smart Charging has identified that this is an optimal time to charge - SMART_CHARGING_DEADLINE - because, regardless of price, charging must be active to meet the configured deadline |  [optional] |
|**isPluggedIn** | **Boolean** | Indicates whether the vehicle is connected to a charging box (regardless of whether it is actually charging) |  [optional] |
|**range** | **BigDecimal** | Estimated remaining kilometers |  [optional] |



## Enum: List&lt;IsChargingReasonsEnum&gt;

| Name | Value |
|---- | -----|
| _OVERRIDE_TRUE_ | &quot;{\&quot;override\&quot;:true}&quot; |
| DEFAULT | &quot;DEFAULT&quot; |



