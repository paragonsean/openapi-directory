

# OutlierDetection

A form of passive health checking that dynamically determines whether instances in a cluster are performing unlike others and preemptively removes them from a load balancing set. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseEjectionTimeMsec** | **Integer** | The base time that a host is ejected for. The real time is equal to the base time multiplied by the number of times the host has been ejected. Defaults to 30s. Setting this to 0 means that no host will be ejected for longer than &#x60;interval_msec&#x60;.  |  [optional] |
|**consecutive5xx** | **Integer** | The number of consecutive 5xx responses before a consecutive 5xx ejection occurs. Defaults to 5. Setting this to 0 effectively turns off the consecutive 5xx detector.  |  [optional] |
|**consecutiveGatewayFailure** | **Integer** | The number of consecutive gateway failures (502, 503, 504 status or connection errors that are mapped to one of those status codes) before a consecutive gateway failure ejection occurs. Defaults to 5. Setting this to 0 effectively turns off the consecutive gateway failure detector.  |  [optional] |
|**enforcingConsecutive5xx** | **Integer** | The % chance that a host will be actually ejected when an outlier status is detected through consecutive 5xx. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100.  |  [optional] |
|**enforcingConsecutiveGatewayFailure** | **Integer** | The % chance that a host will be actually ejected when an outlier status is detected through consecutive gateway failures. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 0.  |  [optional] |
|**enforcingSuccessRate** | **Integer** | The % chance that a host will be actually ejected when an outlier status is detected through success rate statistics. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100.  |  [optional] |
|**intervalMsec** | **Integer** | The time interval between ejection analysis sweeps. This can result in both new ejections due to success rate outlier detection as well as hosts being returned to service. Defaults to 10s and must be greater than 0.  |  [optional] |
|**maxEjectionPercent** | **Integer** | The maximum % of an upstream cluster that can be ejected due to outlier detection. Defaults to 10% but will always eject at least one host.  |  [optional] |
|**successRateMinimumHosts** | **Integer** | The number of hosts in a cluster that must have enough request volume to detect success rate outliers. If the number of hosts is less than this setting, outlier detection via success rate statistics is not performed for any host in the cluster. Defaults to 5. Setting this to 0 effectively triggers the success rate detector regardless of the number of valid hosts during an interval (as determined by &#x60;success_rate_request_volume&#x60;).  |  [optional] |
|**successRateRequestVolume** | **Integer** | The minimum number of total requests that must be collected in one interval (as defined by interval_msec) to include this host in success rate based outlier detection. If the volume is lower than this setting, outlier detection via success rate statistics is not performed for that host. Defaults to 100. Must be greater than 0.  |  [optional] |
|**successRateStdevFactor** | **Integer** | This factor is used to determine the ejection threshold for success rate outlier ejection. The ejection threshold is the difference between the mean success rate, and the product of this factor and the standard deviation of the mean success rate: mean - (stdev * success_rate_stdev_factor). This factor is divided by a thousand to get a double. That is, if the desired factor is 1.9, the runtime value should be 1900. Defaults to 1900. Setting this to 0 effectively turns off the success rate detector.  |  [optional] |



