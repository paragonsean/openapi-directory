# USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.Eff03

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dischargeMonitoringReports** | [**[Eff01]**](Eff01.md) | An array of Discharge Monitoring Report (DMR) data. | 
**monitoringLocationCode** | **String** | The code that the monitoring location at which the monitoring requirement (and effluent limit if limited) applies. One parameter may have several monitoring location codes pertaining to the same permitted feature | 
**monitoringLocationDesc** | **String** | The name of the monitoring location at which the monitoring requirement (and effluent limit if limited) applies | 
**parameterCode** | **String** | The unique 5 digit numeric code identifying the parameter. If the code is less than 5 digits in the .CSV, append zeros to the beginning of the number (e.g., 100 is equivalent to 00100) | 
**parameterDesc** | **String** | The pollutant name and form (e.g., dissolved, suspended) associated with the parameter code | 
**stayTypeCode** | **String** | The unique identifier of the type of stay applied to a limit (e.g., X, Y, Z), which indicates whether the limits do not appear on the DMR at all, are treated as monitor only, or have a stay value in effect during the period of the stay | 
**stayTypeDesc** | **String** | The name of the type of stay applied to a limit, which indicates whether the limits do not appear on the DMR at all (X), are treated as monitor only (Y), or have a stay value in effect during the period of the stay (Z) | 


