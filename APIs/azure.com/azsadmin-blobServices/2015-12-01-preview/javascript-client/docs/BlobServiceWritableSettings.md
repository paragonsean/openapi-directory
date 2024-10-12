# StorageManagementClient.BlobServiceWritableSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blobSvcContainerGcInterval** | **Number** | The interval, in seconds, of container garbage collection. | [optional] [readonly] 
**blobSvcShallowGcInterval** | **Number** | The interval ,in seconds, of shallow garbage collection. | [optional] [readonly] 
**blobSvcStreamMapMinContainerOccupancyPercent** | **Number** | The minimal container occupancy percent for stream mapping. | [optional] [readonly] 
**frontEndHttpListenPort** | **Number** | The HTTP port of the storage service front end. | [optional] 
**frontEndHttpsListenPort** | **Number** | The HTTPs port of the storage service front end. | [optional] 
**frontEndCallbackThreadsCount** | **Number** | Front end callback threads count. | [optional] 
**frontEndCpuBasedKeepAliveThrottlingCpuMonitorIntervalInSeconds** | **Number** | Interval (in second) of CPU monitor for front end CPU based keep-alive throttling. | [optional] 
**frontEndCpuBasedKeepAliveThrottlingEnabled** | **Boolean** | Switch of front end CPU based keep-alive throttling. | [optional] 
**frontEndCpuBasedKeepAliveThrottlingPercentCpuThreshold** | **Number** | Threshold (% percentage) of front end CPU based keep-alive throttling. | [optional] 
**frontEndCpuBasedKeepAliveThrottlingPercentRequestsToThrottle** | **Number** | Threshold (% percentage) of requests to throttle in front end CPU based keep-alive throttling. | [optional] 
**frontEndMaxMillisecondsBetweenMemorySamples** | **Number** | Maximum interval (in millisecond) between memory samples of front end. | [optional] 
**frontEndMemoryThrottleThresholdSettings** | **String** | Front end memory throttle threshold settings. | [optional] 
**frontEndMemoryThrottlingEnabled** | **Boolean** | Switch of front end memory throttling. | [optional] 
**frontEndMinThreadPoolThreads** | **Number** | Front end minimum number of threads in thread pool. | [optional] 
**frontEndThreadPoolBasedKeepAliveIOCompletionThreshold** | **Number** | Threshold of front end thread pool based keep-alive IO completion. | [optional] 
**frontEndThreadPoolBasedKeepAliveMonitorIntervalInSeconds** | **Number** | Monitor interval (in seconds) of front end thread pool based keep-alive monitor. | [optional] 
**frontEndThreadPoolBasedKeepAlivePercentage** | **Number** | Percentage (%) of front end thread pool based keep-alive. | [optional] 
**frontEndThreadPoolBasedKeepAliveWorkerThreadThreshold** | **Number** | Threshold of front end thread pool based keep-alive worker thread. | [optional] 
**frontEndUseSlaTimeInAvailability** | **Boolean** | Switch of whether front end uses SLA time in availability. | [optional] 


