

# DatabaseUpdates

Configuration settings for automated patch update maintenance for the Managed Database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | **Integer** | The day to perform maintenance. 1&#x3D;Monday, 2&#x3D;Tuesday, etc. |  [optional] |
|**duration** | **Integer** | The maximum maintenance window time in hours. |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | Whether maintenance occurs on a weekly or monthly basis. |  [optional] |
|**hourOfDay** | **Integer** | The hour to begin maintenance based in UTC time. |  [optional] |
|**weekOfMonth** | **Integer** | The week of the month to perform &#x60;monthly&#x60; frequency updates. Defaults to &#x60;null&#x60;.  * Required for &#x60;monthly&#x60; frequency updates.  * Must be &#x60;null&#x60; for &#x60;weekly&#x60; frequency updates.  |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |



