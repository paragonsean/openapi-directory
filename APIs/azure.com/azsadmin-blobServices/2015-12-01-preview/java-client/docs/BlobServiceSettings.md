

# BlobServiceSettings

Blob service settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobSvcContainerGcInterval** | **Integer** | The interval, in seconds, of container garbage collection. |  [optional] [readonly] |
|**blobSvcShallowGcInterval** | **Integer** | The interval ,in seconds, of shallow garbage collection. |  [optional] [readonly] |
|**blobSvcStreamMapMinContainerOccupancyPercent** | **Integer** | The minimal container occupancy percent for stream mapping. |  [optional] [readonly] |
|**frontEndHttpListenPort** | **Integer** | The HTTP port of the storage service front end. |  [optional] |
|**frontEndHttpsListenPort** | **Integer** | The HTTPs port of the storage service front end. |  [optional] |
|**frontEndCallbackThreadsCount** | **Integer** | Front end callback threads count. |  [optional] |
|**frontEndCpuBasedKeepAliveThrottlingCpuMonitorIntervalInSeconds** | **Integer** | Interval (in second) of CPU monitor for front end CPU based keep-alive throttling. |  [optional] |
|**frontEndCpuBasedKeepAliveThrottlingEnabled** | **Boolean** | Switch of front end CPU based keep-alive throttling. |  [optional] |
|**frontEndCpuBasedKeepAliveThrottlingPercentCpuThreshold** | **Float** | Threshold (% percentage) of front end CPU based keep-alive throttling. |  [optional] |
|**frontEndCpuBasedKeepAliveThrottlingPercentRequestsToThrottle** | **Float** | Threshold (% percentage) of requests to throttle in front end CPU based keep-alive throttling. |  [optional] |
|**frontEndMaxMillisecondsBetweenMemorySamples** | **Integer** | Maximum interval (in millisecond) between memory samples of front end. |  [optional] |
|**frontEndMemoryThrottleThresholdSettings** | **String** | Front end memory throttle threshold settings. |  [optional] |
|**frontEndMemoryThrottlingEnabled** | **Boolean** | Switch of front end memory throttling. |  [optional] |
|**frontEndMinThreadPoolThreads** | **Integer** | Front end minimum number of threads in thread pool. |  [optional] |
|**frontEndThreadPoolBasedKeepAliveIOCompletionThreshold** | **Integer** | Threshold of front end thread pool based keep-alive IO completion. |  [optional] |
|**frontEndThreadPoolBasedKeepAliveMonitorIntervalInSeconds** | **Integer** | Monitor interval (in seconds) of front end thread pool based keep-alive monitor. |  [optional] |
|**frontEndThreadPoolBasedKeepAlivePercentage** | **Float** | Percentage (%) of front end thread pool based keep-alive. |  [optional] |
|**frontEndThreadPoolBasedKeepAliveWorkerThreadThreshold** | **Integer** | Threshold of front end thread pool based keep-alive worker thread. |  [optional] |
|**frontEndUseSlaTimeInAvailability** | **Boolean** | Switch of whether front end uses SLA time in availability. |  [optional] |



