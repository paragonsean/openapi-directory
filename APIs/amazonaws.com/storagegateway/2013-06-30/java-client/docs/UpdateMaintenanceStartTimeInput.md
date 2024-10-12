

# UpdateMaintenanceStartTimeInput

<p>A JSON object containing the following fields:</p> <ul> <li> <p> <a>UpdateMaintenanceStartTimeInput$DayOfMonth</a> </p> </li> <li> <p> <a>UpdateMaintenanceStartTimeInput$DayOfWeek</a> </p> </li> <li> <p> <a>UpdateMaintenanceStartTimeInput$HourOfDay</a> </p> </li> <li> <p> <a>UpdateMaintenanceStartTimeInput$MinuteOfHour</a> </p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gatewayARN** | **String** | The Amazon Resource Name (ARN) of the gateway. Use the &lt;a&gt;ListGateways&lt;/a&gt; operation to return a list of gateways for your account and Amazon Web Services Region. |  |
|**hourOfDay** | [**Integer**](Integer.md) |  |  |
|**minuteOfHour** | [**Integer**](Integer.md) |  |  |
|**dayOfWeek** | [**Integer**](Integer.md) |  |  [optional] |
|**dayOfMonth** | [**Integer**](Integer.md) |  |  [optional] |



