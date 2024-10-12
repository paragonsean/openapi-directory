

# GoogleChromeManagementV1DeviceAueCountReport

Report for CountChromeDevicesPerAueDateResponse, contains the count of devices of a specific model and auto update expiration range.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aueMonth** | [**AueMonthEnum**](#AueMonthEnum) | Enum value of month corresponding to the auto update expiration date in UTC time zone. If the device is already expired, this field is empty. |  [optional] |
|**aueYear** | **String** | Int value of year corresponding to the Auto Update Expiration date in UTC time zone. If the device is already expired, this field is empty. |  [optional] |
|**count** | **String** | Count of devices of this model. |  [optional] |
|**expired** | **Boolean** | Boolean value for whether or not the device has already expired. |  [optional] |
|**model** | **String** | Public model name of the devices. |  [optional] |



## Enum: AueMonthEnum

| Name | Value |
|---- | -----|
| MONTH_UNSPECIFIED | &quot;MONTH_UNSPECIFIED&quot; |
| JANUARY | &quot;JANUARY&quot; |
| FEBRUARY | &quot;FEBRUARY&quot; |
| MARCH | &quot;MARCH&quot; |
| APRIL | &quot;APRIL&quot; |
| MAY | &quot;MAY&quot; |
| JUNE | &quot;JUNE&quot; |
| JULY | &quot;JULY&quot; |
| AUGUST | &quot;AUGUST&quot; |
| SEPTEMBER | &quot;SEPTEMBER&quot; |
| OCTOBER | &quot;OCTOBER&quot; |
| NOVEMBER | &quot;NOVEMBER&quot; |
| DECEMBER | &quot;DECEMBER&quot; |



