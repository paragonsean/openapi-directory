# LinodeApi.DatabaseUpdates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dayOfWeek** | **Number** | The day to perform maintenance. 1&#x3D;Monday, 2&#x3D;Tuesday, etc. | [optional] 
**duration** | **Number** | The maximum maintenance window time in hours. | [optional] 
**frequency** | **String** | Whether maintenance occurs on a weekly or monthly basis. | [optional] [default to &#39;weekly&#39;]
**hourOfDay** | **Number** | The hour to begin maintenance based in UTC time. | [optional] 
**weekOfMonth** | **Number** | The week of the month to perform &#x60;monthly&#x60; frequency updates. Defaults to &#x60;null&#x60;.  * Required for &#x60;monthly&#x60; frequency updates.  * Must be &#x60;null&#x60; for &#x60;weekly&#x60; frequency updates.  | [optional] 



## Enum: FrequencyEnum


* `weekly` (value: `"weekly"`)

* `monthly` (value: `"monthly"`)




