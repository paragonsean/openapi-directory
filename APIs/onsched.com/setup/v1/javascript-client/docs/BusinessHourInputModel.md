# OnSchedSetupApi.BusinessHourInputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Number** | endTime is entered in military format. e.g. 1800 &#x3D; 6pm end, 2400 &#x3D; midnight end of day.  For 24 hours enter startTime &#x3D; 0 and endTime &#x3D; 2400 | [optional] 
**is24Hours** | **Boolean** | If true then available for 24 hours. startTime must be zero and endTime must be 2400. | [optional] 
**isOpen** | **Boolean** | If false, then not available entire day, starTime and endTime must both be zero. If true, then available between startTime and endTime. | [optional] 
**startTime** | **Number** | startTime is entered in military format. e.g. 0 &#x3D; midnight start, 900 &#x3D; 9am start | [optional] 


