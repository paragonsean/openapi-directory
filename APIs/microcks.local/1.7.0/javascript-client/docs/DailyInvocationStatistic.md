# MicrocksApiV17.DailyInvocationStatistic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dailyCount** | **Number** | The number of service mock invocations on this day | 
**day** | **String** | The day (formatted as yyyyMMdd string) represented by this statistic | 
**hourlyCount** | **{String: Object}** | The number of service mock invocations per hour of the day (keys range from 0 to 23) | [optional] 
**id** | **String** | Unique identifier of this statistic object | 
**minuteCount** | **{String: Object}** | The number of service mock invocations per minute of the day (keys range from 0 to 1439) | [optional] 
**serviceName** | **String** | The name of the service this statistic is related to | 
**serviceVersion** | **String** | The version of the service this statistic is related to | 


