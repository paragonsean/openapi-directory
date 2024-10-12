

# BandwidthRateLimitInterval

 Describes a bandwidth rate limit interval for a gateway. A bandwidth rate limit schedule consists of one or more bandwidth rate limit intervals. A bandwidth rate limit interval defines a period of time on one or more days of the week, during which bandwidth rate limits are specified for uploading, downloading, or both. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startHourOfDay** | [**Integer**](Integer.md) |  |  |
|**startMinuteOfHour** | [**Integer**](Integer.md) |  |  |
|**endHourOfDay** | [**Integer**](Integer.md) |  |  |
|**endMinuteOfHour** | [**Integer**](Integer.md) |  |  |
|**daysOfWeek** | [**List**](List.md) |  |  |
|**averageUploadRateLimitInBitsPerSec** | [**Integer**](Integer.md) |  |  [optional] |
|**averageDownloadRateLimitInBitsPerSec** | [**Integer**](Integer.md) |  |  [optional] |



