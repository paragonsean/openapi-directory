

# DailyInvocationStatistic

The daily statistic of a service mock invocations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dailyCount** | **BigDecimal** | The number of service mock invocations on this day |  |
|**day** | **String** | The day (formatted as yyyyMMdd string) represented by this statistic |  |
|**hourlyCount** | **Map&lt;String, Object&gt;** | The number of service mock invocations per hour of the day (keys range from 0 to 23) |  [optional] |
|**id** | **String** | Unique identifier of this statistic object |  |
|**minuteCount** | **Map&lt;String, Object&gt;** | The number of service mock invocations per minute of the day (keys range from 0 to 1439) |  [optional] |
|**serviceName** | **String** | The name of the service this statistic is related to |  |
|**serviceVersion** | **String** | The version of the service this statistic is related to |  |



