# RocketServices.DeviceRegistrationWindow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endDate** | **Date** | The end date of the current period.  This is based on the value of &#x60;startDate&#x60; plus the number of days defined by  &#x60;periodDays&#x60;.  | 
**limit** | **Number** | The maximum de/registrations that can be made in a period. | 
**periodDays** | **Number** | The number of days a de/registration period runs for. | 
**remaining** | **Number** | The remaining de/registrations that can be made in the current period. | 
**startDate** | **Date** | The start date of the current period.  This is based on the earliest device de/registrations in the past N days, where N is defined by &#x60;periodDays&#x60;.  If no device has been de/registered then start date will be from the current date.  | 


