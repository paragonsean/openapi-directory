

# DeviceRegistrationWindow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endDate** | **OffsetDateTime** | The end date of the current period.  This is based on the value of &#x60;startDate&#x60; plus the number of days defined by  &#x60;periodDays&#x60;.  |  |
|**limit** | **Integer** | The maximum de/registrations that can be made in a period. |  |
|**periodDays** | **Integer** | The number of days a de/registration period runs for. |  |
|**remaining** | **Integer** | The remaining de/registrations that can be made in the current period. |  |
|**startDate** | **OffsetDateTime** | The start date of the current period.  This is based on the earliest device de/registrations in the past N days, where N is defined by &#x60;periodDays&#x60;.  If no device has been de/registered then start date will be from the current date.  |  |



